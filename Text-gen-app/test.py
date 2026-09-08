import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="Gemini Text Generator", page_icon="T")
st.title("Text Generator App")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Add GEMINI_API_KEY to Text-gen-app/.env before running the app.")
    st.stop()

client = genai.Client(api_key=api_key)


def generate_text(prompt, max_tokens, temperature):
    detailed_prompt = (
        f"{prompt}\n\n"
        "Give a paragraph "
        "of approximately 150 to 250 words. Do not stop after the introduction."
    )
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=detailed_prompt,
        config={
            "max_output_tokens": int(max_tokens),
            "temperature": temperature,
            "thinking_config": {
                "thinking_level": "minimal",
            },
        },
    )
    generated_text = (response.text or "").strip()
    if not generated_text:
        return "No text was returned."

    complete_endings = (".", "!", "?", ":", ";", "...", '"', "'", ")", "]")
    if not generated_text.endswith(complete_endings):
        continuation = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=(
                "Continue the following incomplete answer and finish the thought "
                "clearly. Do not repeat the existing text.\n\n"
                f"Existing answer:\n{generated_text}"
            ),
            config={
                "max_output_tokens": int(max_tokens),
                "temperature": temperature,
                "thinking_config": {
                    "thinking_level": "minimal",
                },
            },
        )
        continuation_text = (continuation.text or "").strip()
        if continuation_text:
            generated_text = f"{generated_text} {continuation_text}"

    return generated_text


with st.form("text_generation_form"):
    prompt = st.text_area("Prompt", placeholder="Ask something...", height=140)
    max_tokens = st.slider("Max tokens", 10, 500, 100, 10)
    temperature = st.slider("Temperature", 0.1, 1.5, 0.7, 0.1)
    submitted = st.form_submit_button("Generate")

if submitted:
    if not prompt.strip():
        st.warning("Enter a prompt first.")
    else:
        with st.spinner("Generating..."):
            try:
                st.subheader("Generated text")
                generated_text = generate_text(prompt, max_tokens, temperature)
                st.markdown(generated_text)
            except Exception as error:
                st.error(f"Generation failed: {error}")
