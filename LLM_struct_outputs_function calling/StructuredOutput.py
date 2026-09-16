import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class Product(BaseModel):
    name: str = Field(description="Product name")
    price: float = Field(description="Product price")
    category: str = Field(description="Product category")
    available: bool = Field(description="Whether the product is available")


llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


structured_llm = llm.with_structured_output(Product)


text = """
Looking for a new smartphone? The Google Pixel 9 is being sold
for around ₹79,999. Customers can order it right now.
"""



result = structured_llm.invoke(text)


print("Product Name:", result.name)
print("Price:", result.price)
print("Category:", result.category)
print("Available:", result.available)