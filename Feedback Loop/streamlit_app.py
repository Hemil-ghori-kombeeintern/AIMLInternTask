import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Feedback Loop",
    page_icon="🤖",
    layout="wide"
)


if "response_id" not in st.session_state:
    st.session_state.response_id = None

if "question" not in st.session_state:
    st.session_state.question = None

if "answer" not in st.session_state:
    st.session_state.answer = None

if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False

if "show_comment" not in st.session_state:
    st.session_state.show_comment = False


def ask_ai(question):
    try:
        response = requests.post(
            f"{API_URL}/ask",
            json={"question": question},
            timeout=120
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {e}")
        return None


def send_feedback(response_id, rating, comment=None):
    try:
        response = requests.post(
            f"{API_URL}/feedback",
            json={
                "response_id": response_id,
                "rating": rating,
                "comment": comment
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"Feedback Error: {e}")
        return None


def get_summary():
    try:
        response = requests.get(
            f"{API_URL}/feedback/summary",
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"Summary Error: {e}")
        return None


def get_all_feedback():
    try:
        response = requests.get(
            f"{API_URL}/feedback",
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        st.error(f"Feedback Error: {e}")
        return []



with st.sidebar:

    st.title("🤖 AI Feedback Loop")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "💬 Ask AI",
            "📊 Dashboard",
            "📋 Feedback History"
        ]
    )



if page == "💬 Ask AI":

    st.title("💬 Ask AI")
    st.write("Ask a question and provide feedback on the AI response.")

    st.markdown("---")

    question = st.text_area(
        "Your Question",
        placeholder="Example: What is machine learning?",
        height=120
    )

    if st.button(
        "🚀 Generate Answer",
        type="primary",
        use_container_width=True
    ):

        if not question.strip():
            st.warning("Please enter a question.")

        else:

            with st.spinner("Generating AI response..."):
                result = ask_ai(question)

            if result:
                st.session_state.response_id = result["response_id"]
                st.session_state.question = result["question"]
                st.session_state.answer = result["answer"]
                st.session_state.feedback_submitted = False
                st.session_state.show_comment = False

                st.rerun()


    if st.session_state.answer:

        st.markdown("---")

        st.subheader("🤖 AI Response")

        st.info(st.session_state.answer)

        st.caption(
            f"Response ID: `{st.session_state.response_id}`"
        )

        st.markdown("---")

        st.subheader("Was this answer helpful?")

        col1, col2 = st.columns(2)

        # Positive
        with col1:

            if st.button(
                "👍 Helpful",
                use_container_width=True,
                disabled=st.session_state.feedback_submitted
            ):

                result = send_feedback(
                    st.session_state.response_id,
                    1
                )

                if result:
                    st.session_state.feedback_submitted = True

                    st.success(
                        "Thank you for your feedback! 👍"
                    )

                    st.rerun()

        # Negative
        with col2:

            if st.button(
                "👎 Not Helpful",
                use_container_width=True,
                disabled=st.session_state.feedback_submitted
            ):

                st.session_state.show_comment = True

        # Negative comment
        if st.session_state.show_comment:

            st.markdown("### 📝 What could be improved?")

            comment = st.text_area(
                "Your feedback",
                placeholder="Example: The answer was incomplete...",
                key="negative_comment"
            )

            if st.button(
                "Submit Feedback",
                type="primary"
            ):

                result = send_feedback(
                    st.session_state.response_id,
                    -1,
                    comment
                )

                if result:
                    st.session_state.feedback_submitted = True
                    st.session_state.show_comment = False

                    st.success(
                        "Thank you! Your feedback was recorded."
                    )

                    st.rerun()

elif page == "📊 Dashboard":

    st.title("📊 Feedback Dashboard")

    st.write(
        "Monitor user feedback for AI responses."
    )

    st.markdown("---")

    summary = get_summary()

    if summary:

        total = summary["total_feedback"]
        positive = summary["positive_feedback"]
        negative = summary["negative_feedback"]
        positive_rate = summary[
            "positive_feedback_percentage"
        ]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Feedback", total)
        col2.metric("👍 Positive", positive)
        col3.metric("👎 Negative", negative)
        col4.metric("Positive Rate", f"{positive_rate}%")

        st.markdown("---")

        if total > 0:

            st.subheader("Feedback Distribution")

            chart_data = {
                "Positive": positive,
                "Negative": negative
            }

            st.bar_chart(chart_data)

        else:
            st.info("No feedback available yet.")



elif page == "📋 Feedback History":

    st.title("📋 Feedback History")

    st.write(
        "View all questions, answers and feedback."
    )

    st.markdown("---")

    feedback = get_all_feedback()

    if feedback:

        for item in feedback:

            title = (
                "👍 Positive"
                if item["rating"] == 1
                else "👎 Negative"
            )

            with st.expander(
                f"{title} — {item['question'][:80]}"
            ):

                st.markdown("### Question")
                st.write(item["question"])

                st.markdown("### AI Answer")
                st.info(item["answer"])

                st.markdown("### Feedback")

                if item["rating"] == 1:
                    st.success("👍 Positive Feedback")
                else:
                    st.error("👎 Negative Feedback")

                if item["comment"]:
                    st.markdown("**User Comment:**")
                    st.write(item["comment"])

                st.caption(
                    f"Feedback Time: {item['feedback_time']}"
                )

    else:
        st.info("No feedback records found.")
