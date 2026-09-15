import os

from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

gemini_llm = LLM(
    model="gemini-3.1-flash-lite",
    api_key=os.environ["GEMINI_API_KEY"]
)

# ------------------------------------------------
# 1. Create Researcher Agent
# ------------------------------------------------

researcher = Agent(
    role="AI Researcher",

    goal="Research the given AI topic and provide useful information.",

    backstory="""
    You are an AI researcher.
    You explain technical concepts clearly
    and focus on accurate information.
    """,
    llm=gemini_llm,
    verbose=True
)


# ------------------------------------------------
# 2. Create Writer Agent
# ------------------------------------------------

writer = Agent(
    role="Technical Writer",

    goal="Create a simple and clear report using the research.",

    backstory="""
    You are an experienced technical writer.
    You explain complex AI topics in simple language.
    """,
    llm=gemini_llm,

    verbose=True
)


# ------------------------------------------------
# 3. Create Research Task
# ------------------------------------------------

research_task = Task(
    description="""
    Research the topic:

    {topic}

    Explain:
    1. What it is
    2. How it works
    3. Important concepts
    4. Real-world applications
    """,

    expected_output="""
    A clear research summary about the topic.
    """,

    agent=researcher
)


# ------------------------------------------------
# 4. Create Writing Task
# ------------------------------------------------

writing_task = Task(
    description="""
    Using the research provided by the researcher,
    create a simple technical report about:

    {topic}

    The report should contain:
    - Introduction
    - How it works
    - Applications
    - Conclusion
    """,

    expected_output="""
    A well-structured technical report.
    """,

    agent=writer,
    output_file="final_report.md"
)


# ------------------------------------------------
# 5. Create Crew
# ------------------------------------------------

crew = Crew(
    agents=[researcher,writer],
    tasks=[research_task,writing_task],
    process=Process.sequential,
    max_rpm=10,
    tracing=True,
    verbose=True
)


# ------------------------------------------------
# 6. Start Crew
# ------------------------------------------------

result = crew.kickoff(
    inputs={
        "topic": "Generative AI"
    }
)


# ------------------------------------------------
# 7. Print Result
# ------------------------------------------------

print("\n\n===== FINAL REPORT =====\n")

print(result)