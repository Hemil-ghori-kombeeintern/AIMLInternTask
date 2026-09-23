# from google import genai
# from langsmith import wrappers
# from dotenv import load_dotenv

# load_dotenv()
# client = wrappers.wrap_gemini(
#     genai.Client()
# )

# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents="Explain AI observability in simple words."
# )

# print(response.text)


import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY is missing")

if not os.getenv("LANGSMITH_API_KEY"):
    raise ValueError("LANGSMITH_API_KEY is missing")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0,
)

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI assistant.

    Answer the following question clearly and simply.

    Question: {question}
    """
)



chain = prompt | llm


def ask_question(question: str):
    
    response = chain.invoke(
        {"question": question}
    )

    return response.content


if __name__ == "__main__":
    question = input("Enter your question: ")

    answer = ask_question(question)

    print("\nAI Answer:")
    print(answer)