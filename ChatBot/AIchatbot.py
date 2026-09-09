import os
import streamlit as st

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:

    st.error("GEMINI_API_KEY is not configured.")

    st.stop()


client = genai.Client(
    api_key=API_KEY
)


st.set_page_config(
    page_title="AI/ML Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 AI/ML Chatbot")

st.caption(
    "Chat with AI/ML Chatbot"
)

SYSTEM_INSTRUCTION = """
You are a helpful AI/ML assistant.

Rules:
- Explain concepts clearly.
- Use simple language.
- Give examples when useful.
- Provide clean Python code when requested.
- Stay focused on the user's question.
"""


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


user_input = st.chat_input(
    "Ask something about AI/ML..."
)


if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):

        st.markdown(user_input)

    contents = []

    for message in st.session_state.messages:

        role = message["role"]

        if role == "assistant":
            role = "model"

        contents.append({
            "role": role,
            "parts": [
                {
                    "text": message["content"]
                }
            ]
        })


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=contents,
                config={
                    "system_instruction": SYSTEM_INSTRUCTION
                }
            )

            answer = response.text

            st.markdown(answer)


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })