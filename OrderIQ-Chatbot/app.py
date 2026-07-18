import streamlit as st
from bot import get_response

st.set_page_config(page_title="OrderIQ - E-Commerce Chatbot", page_icon="🛒")
st.title("🛒 OrderIQ - E-Commerce Chatbot")
st.caption("Ask me about orders, products, coupons, revenue, or referrals.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})