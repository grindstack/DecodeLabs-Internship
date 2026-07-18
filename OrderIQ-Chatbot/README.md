# OrderIQ — Intelligent E-Commerce Chatbot 🛒

A hybrid AI chatbot that combines rule-based logic, pandas data queries, and a local LLM fallback (Ollama) to answer e-commerce questions through a clean Streamlit chat interface.

## Project Structure

```
OrderIQ-Chatbot/
├── app.py              # Streamlit UI
├── bot.py              # Core logic — rules, orchestration, Ollama fallback
├── data_queries.py     # Pandas-based CSV queries
├── dataset.csv         # E-commerce orders dataset (1,200 records)
├── requirements.txt    # Dependencies
└── .gitignore
```

## Architecture

The bot processes every message through 3 layers in order:

```
User Input
    ↓
Layer 1 — Rule-Based Responses
    ↓ (no match)
Layer 2 — Pandas Data Queries
    ↓ (no match)
Layer 3 — Ollama LLM Fallback
```

## Features

- **Order status lookup** — query any order by ID
- **Coupon information** — details and usage stats for SAVE10, FREESHIP, WINTER15
- **Product catalogue** — list all available products
- **Cancellation analytics** — find the most cancelled product
- **Referral insights** — identify top traffic source
- **Revenue analytics** — total revenue by year or all-time
- **LLM fallback** — handles open-ended questions via Ollama

## Dataset

1,200 e-commerce orders with 14 columns including OrderID, Date, Product, Quantity, UnitPrice, TotalPrice, OrderStatus, PaymentMethod, CouponCode, and ReferralSource.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Chat UI |
| Pandas | Data queries |
| Ollama + llama3.2 | Local LLM fallback |
| Regex | Input parsing |

## Run Locally

Prerequisites: Python 3.10+ and [Ollama](https://ollama.com) installed with llama3.2 pulled.

```bash
git clone https://github.com/grindstack/DecodeLabs-Internship.git
cd DecodeLabs-Internship/OrderIQ-Chatbot
pip install -r requirements.txt
ollama serve
streamlit run app.py
```

## Example Queries

```
What's the status of my order ORD200005?
What products do you sell?
I used coupon SAVE10, what's the discount?
Which product gets cancelled the most?
What's the total revenue in 2023?
What's our most popular referral source?
```

## What I Learned

- Rule-based AI systems and their limitations
- Integrating a local LLM as an intelligent fallback
- Pandas for real-time data querying from user input
- Word boundary matching with regex to avoid false rule triggers
- Building a chat UI with Streamlit
- Clean separation of concerns across multiple Python modules

## Author

**Fatimah** — AI Engineering Intern @ DecodeLabs  
