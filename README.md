# Blog Post Generator

> **Note:** This project is still a work in progress and I will enhance it in the future.

This is a Streamlit web application that generates a blog post outline and an engaging introduction using OpenAI's GPT-4o model via LangChain.

## Features
- Enter a topic to generate a blog post outline.
- Automatically creates an engaging introduction paragraph based on the outline.
- Powered by OpenAI and LangChain.

## Requirements
- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [langchain-openai](https://python.langchain.com/docs/integrations/llms/openai)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install streamlit langchain langchain-openai python-dotenv
   ```
3. **Create a `.env` file** in the project root with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. **Run the app:**
   ```bash
   streamlit run blog_post.py
   ```

## Usage
- Enter a topic in the input field.
- The app will display a blog outline and an introduction paragraph.
