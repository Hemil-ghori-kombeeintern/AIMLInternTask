import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from google import genai
from eval.eval_metrics import evaluate_single_response

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY is not configured.")
    st.stop()

client = genai.Client(api_key=API_KEY)

st.set_page_config(
    page_title="AI/ML Chatbot with DeepEval",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI/ML Chatbot")
st.caption("Powered by Gemini Flash Lite & DeepEval 9-Metric LLM Evaluation")

# Sidebar Configuration for Gemini Models & DeepEval
with st.sidebar:
    st.header("⚙️ Model Configuration")
    
    # Model Selection (Only Gemini 3.1 Flash Lite and Gemini 3.5 Flash Lite)
    chatbot_model = st.selectbox(
        "🤖 Chatbot Model",
        ["gemini-3.1-flash-lite", "gemini-3.5-flash-lite"],
        index=0
    )
    
    st.header("📊 DeepEval Evaluation Settings")
    
    # Toggle button to enable/disable real-time LLM evaluation calculation
    enable_eval = st.toggle("Enable Real-time Evaluation", value=True, key="enable_eval")
    
    # Toggle button to show/hide the evaluation metric cards/tables in chat UI
    show_eval_cards = st.toggle("Show Evaluation Table in Chat", value=True, key="show_eval_cards")
    
    # Evaluator Judge Model Selection (Only Gemini 3.1 Flash Lite and Gemini 3.5 Flash Lite)
    judge_model = st.selectbox(
        "⚖️ Evaluator Judge Model",
        ["gemini-3.1-flash-lite", "gemini-3.5-flash-lite"],
        index=0
    )
    
    # st.markdown("---")
    # st.markdown("""
    # **📋 9 Metrics Evaluated:**
    # 1. 🎯 Answer Relevancy
    # 2. 📜 Faithfulness
    # 3. 🔍 Contextual Relevancy
    # 4. 🎯 Contextual Precision
    # 5. 📌 Contextual Recall
    # 6. ✅ Correctness
    # 7. 👻 Hallucination
    # 8. 🛡️ Toxicity
    # 9. ⚖️ Bias
    # """)

SYSTEM_INSTRUCTION = """
You are a helpful AI/ML assistant.

Rules:
- Explain concepts clearly and simply.
- Use simple language.
- Give examples when useful.
- Provide clean Python code when requested.
- Stay focused on the user's question.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []


def display_eval_table(eval_results: dict):
    """Renders formatted evaluation metrics inside a Streamlit table."""
    with st.expander("📊 **DeepEval 9-Metric Evaluation Table**", expanded=True):
        table_rows = []
        for metric_name, data in eval_results.items():
            table_rows.append({
                "Metric": metric_name,
                "Score": f"{data['score']:.3f}",
                "Status": "✅ PASS" if data["passed"] else "❌ FAIL",
                "Reason": data["reason"]
            })
        
        df = pd.DataFrame(table_rows)
        st.dataframe(
            df,
            column_config={
                "Metric": st.column_config.TextColumn("Evaluation Metric", width="medium"),
                "Score": st.column_config.TextColumn("Score (0.0 - 1.0)", width="small"),
                "Status": st.column_config.TextColumn("Status", width="small"),
                "Reason": st.column_config.TextColumn("Evaluator Reason", width="large")
            },
            use_container_width=True,
            hide_index=True
        )


# Display message history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if show_eval_cards and "eval_results" in message and message["eval_results"]:
            display_eval_table(message["eval_results"])

user_input = st.chat_input("Ask something about AI/ML...")

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

        # Exclude eval_results key when formatting contents for Gemini API
        contents.append({
            "role": role,
            "parts": [{"text": message["content"]}]
        })

    with st.chat_message("assistant"):
        with st.spinner(f"Thinking using {chatbot_model}..."):
            from eval.eval_gemini import global_rpm_limiter
            global_rpm_limiter.wait_if_needed()
            response = client.models.generate_content(
                model=chatbot_model,
                contents=contents,
                config={"system_instruction": SYSTEM_INSTRUCTION}
            )
            answer = response.text
            st.markdown(answer)

        eval_results = None
        if enable_eval:
            with st.spinner("🔍 Running 9 DeepEval Evaluation Metrics..."):
                try:
                    eval_results = evaluate_single_response(
                        user_input=user_input,
                        actual_output=answer,
                        judge_model_name=judge_model
                    )
                    if show_eval_cards:
                        display_eval_table(eval_results)
                except Exception as e:
                    st.warning(f"DeepEval Evaluation Warning: {str(e)}")

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "eval_results": eval_results
    })