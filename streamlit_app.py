import streamlit as st
import requests

st.set_page_config(page_title="TailorTalk Bot", page_icon="🤖")
st.title("📅 TailorTalk: Book Appointments with AI")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me to book a meeting or check availability...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        res = requests.post("http:tailottalk-production.up.railway.app", json={"message": user_input})
        bot_response = res.json().get("response", "No response")
        st.session_state.chat_history.append(("bot", bot_response))

for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
