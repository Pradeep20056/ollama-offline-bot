import streamlit as st
from chatbot.ollama_bot import OllamaBot

st.set_page_config(page_title="Ollama Chatbot", layout="centered")
st.title("🧠 Local AI Chatbot (Mistral)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

bot = OllamaBot(model="phi")

user_input = st.text_input("You:", "")

if st.button("Send") and user_input.strip():
    reply = bot.chat(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", reply))

st.markdown("### Conversation")
for role, msg in reversed(st.session_state.chat_history):
    st.markdown(f"**{role}:** {msg}")
