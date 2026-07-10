import requests
import re
import pandas as pd
from data_queries import query_data, df

# ── Layer 1 ──────────────────────────────────────────
def get_rule_response(user_input):
    user_input = user_input.lower().strip()
    
    rules = {
        ("hi", "hello", "hey"):       "Hey! How can I help you?",
        ("bye", "exit", "quit"):      "Goodbye!",
        ("your name", "who are you"): "I'm an e-commerce order assistant!",
        ("help",):                    "Ask me about orders, products, revenue, or referrals.",
        ("thank", "thanks"):          "You're welcome!",
    }
    
    for keywords, response in rules.items():
        if any(re.search(rf'\b{word}\b', user_input) for word in keywords):
            return response
    
    return None

# ── Layer 3 ──────────────────────────────────────────
def get_ollama_response(user_input):
    # Build context from dataset
    context = f"""
You are an e-commerce assistant. Answer ONLY from this data:

Products we sell: {', '.join(df['Product'].unique())}
Order statuses possible: {', '.join(df['OrderStatus'].unique())}
Payment methods: {', '.join(df['PaymentMethod'].unique())}
Available coupons: SAVE10 (10% off), FREESHIP (free shipping), WINTER15 (15% off)
Total orders in system: {len(df)}
Price range: ${df['UnitPrice'].min():.2f} to ${df['UnitPrice'].max():.2f}

If the answer is not in this data, say: 
"I don't have that information. I can help with orders, products, coupons, revenue, or referrals."

User question: {user_input}
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": context,
                "stream": False,
            }
        )
        return response.json()["response"]
    except Exception as e:
        return f"Ollama error: {str(e)}"

# ── Orchestrator ──────────────────────────────────────
def get_response(user_input):
    # Layer 1 — rules
    rule = get_rule_response(user_input)
    if rule:
        return rule
    
    # Layer 2 — data queries
    data = query_data(user_input)
    if data:
        return data
    
    # Layer 3 — Ollama fallback
    return get_ollama_response(user_input)

# ── Main loop ─────────────────────────────────────────
if __name__ == "__main__":
    print("Chatbot ready! Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if not user_input.strip():        # ← add this
          continue 
        if user_input.lower() in ("quit", "exit", ":q"):
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}\n")