import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import date, time
from dotenv import load_dotenv
import os


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "Streamlit AI/ML Demo"
)


st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


if "counter" not in st.session_state:
    st.session_state.counter = 0

if "messages" not in st.session_state:
    st.session_state.messages = []

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []


@st.cache_data
def create_sample_data():

    np.random.seed(42)

    data = pd.DataFrame({
        "Student": ["Rahul","Amit","Priya","Neha","Raj","Karan","Meera","Jay"],

        "Study_Hours": [
            5, 3, 8, 6, 2, 7, 9, 4
        ],

        "Attendance": [
            80, 65, 92, 85, 55, 88, 95, 70
        ],

        "Marks": [
            75, 55, 90, 82, 45, 88, 95, 65
        ]
    })

    return data

@st.cache_resource
def load_demo_model():

    def model(study_hours, attendance):
        score = (
            study_hours * 5
            + attendance * 0.5
        )

        if score >= 65:
            return "Pass"

        return "Fail"

    return model


model = load_demo_model()



st.sidebar.title("⚙️ Settings")
st.sidebar.write("Streamlit Demo Application")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Home",
        "Widgets",
        "Data Analysis",
        "ML Prediction",
        "Chatbot",
        "File Upload"
    ]
)


st.sidebar.markdown("---")


# ============================================================
# HOME PAGE
# ============================================================

if page == "Home":

    st.title("🤖 Streamlit AI/ML Demo")

    st.header("Welcome")

    st.subheader(
        "Complete Streamlit Example"
    )

    st.write(
        """
        This application demonstrates the most important
        Streamlit features used in AI/ML applications.
        """
    )

    st.markdown("""
    ### What is Streamlit?

    Streamlit is a Python framework used to create
    interactive web applications and dashboards.

    **Python → Streamlit → Web Application**
    """)

    st.info(
        "Use the sidebar to explore different features.(info)"
    )

    st.success(
        "Streamlit application started successfully!(success)"
    )

    st.warning(
        "This is a learning/demo application.(warning)"
    )

    st.error(
        "This is an example error message.(error)"
    )

    st.markdown("---")

    st.header("Application Architecture")

    st.code(
        """
        User
          ↓
        Streamlit UI
          ↓
        Python
          ↓
        ML / AI / RAG / Database
          ↓
        Result
        """,
        language="text"
    )

    st.header("Quick Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Students",
            "100"
        )

    with col2:
        st.metric(
            "Accuracy",
            "92%"
        )

    with col3:
        st.metric(
            "Models",
            "5"
        )

    with col4:
        st.metric(
            "Status",
            "Online"
        )

    st.markdown("---")

    st.header("Container Example")

    with st.container():

        st.write(
            "Everything inside this container belongs to the same section."
        )

        st.write(
            "Containers are useful for organizing UI elements."
        )


# ============================================================
# WIDGETS PAGE
# ============================================================

elif page == "Widgets":

    st.title("🎛️ Streamlit Widgets")

    st.header("Text Input")

    name = st.text_input("Enter your name")

    if name:
        st.write(
            f"Hello, {name}! 👋"
        )


    st.header("Text Area")
    message = st.text_area("Enter a message")
    if message:
        st.write(
            "Your message:",
            message
        )


    st.header("Number Input")
    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        value=22
    )
    st.write("Age:",age)


    st.header("Slider")

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1
    )

    st.write(
        "Selected temperature:",
        temperature
    )


    st.header("Selectbox")

    model_name = st.selectbox(
        "Select ML Model",
        [
            "Random Forest",
            "Logistic Regression",
            "SVM",
            "Neural Network"
        ]
    )

    st.write(
        "Selected model:",
        model_name
    )


    st.header("Multiselect")

    skills = st.multiselect(
        "Select your skills",
        [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Computer Vision",
            "Generative AI"
        ]
    )

    st.write(
        "Selected skills:",
        skills
    )


    st.header("Radio")

    experience = st.radio(
        "Experience Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    st.write(
        "Experience:",
        experience
    )


    st.header("Checkbox")

    agree = st.checkbox(
        "I agree to continue"
    )

    if agree:

        st.success(
            "You agreed!"
        )


    st.header("Date Input")

    selected_date = st.date_input(
        "Select date",
        date.today()
    )

    st.write(
        "Selected date:",
        selected_date
    )


    st.header("Time Input")

    selected_time = st.time_input(
        "Select time",
        time(10, 0)
    )

    st.write(
        "Selected time:",
        selected_time
    )


    st.header("Button")

    if st.button("Click Me"):

        st.session_state.counter += 1

        st.success(
            f"Button clicked {st.session_state.counter} times."
        )

    st.write("Counter:",st.session_state.counter)


    # ============================================================
    # DATA ANALYSIS PAGE
    # ============================================================

elif page == "Data Analysis":

    st.title("📊 Data Analysis")

    st.header("Sample Dataset")

    df = create_sample_data()

    st.dataframe(
        df,
        use_container_width=True
    )

    st.header("Static Table")

    st.table(df.head(5))


    # ----------------------------------------
    # Metrics
    # ----------------------------------------

    st.header("Dataset Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Students",
            len(df)
        )

    with col2:

        st.metric(
            "Average Marks",
            round(df["Marks"].mean(), 2)
        )

    with col3:

        st.metric(
            "Average Attendance",
            round(df["Attendance"].mean(), 2)
        )

    with col4:

        st.metric(
            "Highest Marks",
            df["Marks"].max()
        )


    # ----------------------------------------
    # Charts
    # ----------------------------------------

    st.header("Charts")

    st.subheader("Line Chart")

    line_data = df.set_index("Student")[
        ["Marks"]
    ]

    st.line_chart(
        line_data
    )


    st.subheader("Bar Chart")

    bar_data = df.set_index("Student")[
        ["Marks"]
    ]

    st.bar_chart(
        bar_data
    )


    st.subheader("Area Chart")

    area_data = df.set_index("Student")[
        ["Study_Hours", "Attendance"]
    ]

    st.area_chart(
        area_data
    )


    # ----------------------------------------
    # Matplotlib
    # ----------------------------------------

    st.subheader(
        "Matplotlib Chart"
    )

    fig, ax = plt.subplots()

    ax.scatter(
        df["Study_Hours"],
        df["Marks"]
    )

    ax.set_xlabel(
        "Study Hours"
    )

    ax.set_ylabel(
        "Marks"
    )

    ax.set_title(
        "Study Hours vs Marks"
    )

    st.pyplot(fig)


    # ----------------------------------------
    # Expander
    # ----------------------------------------

    with st.expander(
        "🔍 Show Dataset Details"
    ):

        st.write(
            "Number of rows:",
            len(df)
        )

        st.write(
            "Number of columns:",
            len(df.columns)
        )

        st.write(
            "Columns:",
            list(df.columns)
        )

        st.write(
            "Data types:"
        )

        st.write(
            df.dtypes
        )


# ============================================================
# ML PREDICTION PAGE
# ============================================================

elif page == "ML Prediction":

    st.title("🧠 ML Prediction")

    st.write(
        "Predict whether a student is likely to pass."
    )


    col1, col2 = st.columns(2)


    with col1:

        study_hours = st.number_input(
            "Study Hours",
            min_value=0.0,
            max_value=24.0,
            value=5.0
        )


    with col2:

        attendance = st.slider(
            "Attendance (%)",
            min_value=0,
            max_value=100,
            value=75
        )


    if st.button("Predict",type="primary"):

        with st.spinner("Running ML model..."):

            prediction = model(
                study_hours,
                attendance
            )


        st.progress(
            min(
                int(
                    study_hours / 24 * 100
                ),
                100
            )
        )


        if prediction == "Pass":

            st.success(
                "Prediction: PASS 🎉"
            )

        else:

            st.error(
                "Prediction: FAIL"
            )


        # Store prediction
        st.session_state.prediction_history.append(
            {
                "Study Hours": study_hours,
                "Attendance": attendance,
                "Prediction": prediction
            }
        )


    st.header(
        "Prediction History"
    )

    if st.session_state.prediction_history:

        history_df = pd.DataFrame(
            st.session_state.prediction_history
        )

        st.dataframe(
            history_df,
            use_container_width=True
        )

    else:

        st.info(
            "No predictions yet."
        )


# ============================================================
# CHATBOT PAGE
# ============================================================

elif page == "Chatbot":

    st.title("🤖 Streamlit Chatbot")

    st.write(
        "Simple chatbot demonstrating session state."
    )


    # ----------------------------------------
    # Display previous messages
    # ----------------------------------------

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )


    # ----------------------------------------
    # Chat input
    # ----------------------------------------

    user_input = st.chat_input(
        "Ask something..."
    )


    if user_input:

        # Store user message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )


        # Display user message

        with st.chat_message("user"):

            st.write(
                user_input
            )


        # ------------------------------------
        # Demo AI response
        # ------------------------------------

        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "Thinking..."
            ):

                if "python" in user_input.lower():

                    answer = (
                        "Python is a popular programming "
                        "language used in AI, ML, web development "
                        "and automation."
                    )

                elif "streamlit" in user_input.lower():

                    answer = (
                        "Streamlit is a Python framework for "
                        "building interactive web applications."
                    )

                else:

                    answer = (
                        f"You asked: {user_input}"
                    )


                st.write(
                    answer
                )


        # Store assistant message

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


# ============================================================
# FILE UPLOAD PAGE
# ============================================================

elif page == "File Upload":

    st.title("📁 File Upload")

    st.header("Upload CSV")


    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"]
    )


    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")

        with st.spinner("Reading CSV..."):

            uploaded_df = pd.read_csv(uploaded_file)


        st.subheader(
            "Uploaded Data"
        )

        st.dataframe(
            uploaded_df,
            use_container_width=True
        )


        st.subheader(
            "Dataset Information"
        )

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Rows",
                uploaded_df.shape[0]
            )


        with col2:

            st.metric(
                "Columns",
                uploaded_df.shape[1]
            )


        with col3:

            st.metric(
                "Missing Values",
                int(
                    uploaded_df.isnull()
                    .sum()
                    .sum()
                )
            )


        with st.expander(
            "Show Dataset Information"
        ):

            st.write(
                uploaded_df.describe()
            )


        # ------------------------------------
        # Charts if numeric columns exist
        # ------------------------------------

        numeric_columns = (
            uploaded_df
            .select_dtypes(include=np.number)
            .columns
        )


        if len(numeric_columns) > 0:

            st.header(
                "Numeric Data Visualization"
            )

            selected_column = st.selectbox(
                "Select column",
                numeric_columns
            )


            st.line_chart(
                uploaded_df[
                    [selected_column]
                ]
            )


        else:

            st.warning(
                "No numeric columns available for charting."
            )


        # ------------------------------------
        # Display raw CSV
        # ------------------------------------

        with st.expander(
            "Show Raw Data"
        ):

            st.write(
                uploaded_df
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Streamlit AI/ML Learning Project"
)