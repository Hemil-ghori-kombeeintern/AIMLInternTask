import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.document_loaders import TextLoader
from langchain_core.tools import tool
from langchain.agents import create_agent


# ============================================================
# 1. LOAD API KEY
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env"
    )


# ============================================================
# 2. CALCULATOR TOOL
# ============================================================

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception:
        return "Could not calculate the expression."


# ============================================================
# 3. COMPANY INFORMATION TOOL
# ============================================================

@tool
def search_company(query: str) -> str:
    """Search internal company information."""
    document_path = os.path.join(
        os.path.dirname(__file__),
        "company_info.txt"
    )

    try:
        loader = TextLoader(
            document_path,
            encoding="utf-8"
        )
        documents = loader.load()
        company_information = "\n\n".join(
            document.page_content
            for document in documents
        )

    except OSError:
        return "The company information document could not be read."

    query_words = {
        word.lower().strip(".,?!")
        for word in query.split()
    }

    matching_lines = [
        line.strip()
        for line in company_information.splitlines()
        if line.strip()
        and any(word in line.lower() for word in query_words)
    ]

    if matching_lines:
        return "\n".join(matching_lines)

    return company_information


# ============================================================
# 4. FREE WEB SEARCH TOOL
# ============================================================

web_search = DuckDuckGoSearchRun()


# ============================================================
# 5. CREATE GEMINI MODEL
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=api_key
)


# ============================================================
# 6. GIVE TOOLS TO SINGLE AGENT
# ============================================================

tools = [calculator,search_company,web_search]

# ============================================================
# 7. CREATE SINGLE AGENT
# ============================================================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""

You are a helpful AI assistant.

You have access to three tools.

1. calculator
   Use this for mathematical calculations.

2. search_company
   Use this for internal company information.

3. web_search
   Use this when the user asks for:
   - latest information
   - current information
   - news
   - internet information
   - information you don't know

Choose the appropriate tool automatically.

You can use multiple tools if necessary.

Give a clear and concise final answer.
"""
)


# ============================================================
# 8. USER QUESTION
# ============================================================

question = input(
    "Ask something: "
)


# ============================================================
# 9. RUN AGENT
# ============================================================

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
)


# 10. PRINT FINAL ANSWER


used_tools = [
    tool_call["name"]
    for message in result["messages"]
    for tool_call in getattr(message, "tool_calls", [])
]

print(f"\nModel used: {llm.model}")
print(
    "Tools used: "
    + (", ".join(dict.fromkeys(used_tools)) if used_tools else "None")
)
print("\nAgent Answer:")

print(
    result["messages"][-1].content[0]["text"]
)