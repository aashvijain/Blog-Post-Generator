from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()  # Loads variables from .env into environment
openai_api_key = os.getenv("OPENAI_API_KEY")
print(f"OpenAI API Key: {openai_api_key}")

llm = ChatOpenAI(model="gpt-4o", api_key=openai_api_key)

outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template= """You are a professional blogger.
Create an outline for a blog post on the following topic: {topic}
The outline should include:
- Introduction
- 3 main points with subpoints
- Conclusion"""
)  

blog_prompt = PromptTemplate(
    input_variables=["outline"],
    template= """You are a professional blogger.
Write an engaging introduction paragraph based on the following
outline:{outline}
The introduction should hook the reader and provide a brief
overview of the topic."""
)  

first_chain = outline_prompt | llm | StrOutputParser() 
second_chain = blog_prompt | llm 
final_chain = first_chain | second_chain

st.title("Blog Generator")

topic = st.text_input("Enter the topic:")

if topic:
    response = final_chain.invoke({"topic": topic})
    st.write(response.content)