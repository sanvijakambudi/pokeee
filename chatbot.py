import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv


st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("Sanvi's Chatbot")


load_dotenv(override=True)
API_KEY = os.getenv("API_KEY")


if not API_KEY:
    try:
        API_KEY = st.secrets["API_KEY"]
    except Exception:
        API_KEY = None

if not API_KEY:
    st.error("No API Key found! Please add it to your .env file or Streamlit secrets.")
    st.stop()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


for message in st.session_state.chat_session.history:

    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)


if prompt := st.chat_input("How can I help you today?"):

    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")