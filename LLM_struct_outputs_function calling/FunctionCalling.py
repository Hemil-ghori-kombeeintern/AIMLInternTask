import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


load_dotenv()
 
@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.2
)


llm_with_tools = llm.bind_tools([add, multiply, subtract])
question = "What is 25 * 50?"


response = llm_with_tools.invoke(question)

if response.tool_calls:

    for tool_call in response.tool_calls:

        tool_name = tool_call["name"]

        arguments = tool_call["args"]

        print("Tool selected:", tool_name)
        print("Arguments:", arguments)

        if tool_name == "add":
            result = add.invoke(arguments)
            print("Tool result:", result)

        elif tool_name == "multiply":
            result = multiply.invoke(arguments)
            print("Tool result:", result)

        elif tool_name == "subtract":
            result = subtract.invoke(arguments)
            print("Tool result:", result)

else:
    print("AI Answer:")
    print(response.content)