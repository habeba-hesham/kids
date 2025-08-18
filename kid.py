import os
import streamlit as st
from transformers import pipeline

st.title("🤖 Kid-Friendly Chatbot via Hugging Face API")

api_token = os.getenv("HF_TOKEN")
model_name = "shashankverma590/tiny-llama-1b-kid-friendly-chatbot-tiny"

chatbot = pipeline("text-generation", model=model_name, use_auth_token=api_token)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = chatbot(user_input, max_length=50)[0]['generated_text']

    st.session_state.messages.append({"role": "bot", "content": response})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"🤖: {msg['content']}")


