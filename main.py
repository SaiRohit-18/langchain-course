import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()

# 2. Create the model
# llm = ChatOllama(
#     model=os.getenv("OLLAMA_MODEL", "gpt-oss:20b-cloud"),
#     base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
#     temperature=0.7,
# )
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

# 3. Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains things simply."),
    ("human", "Explain {topic} in 3 short bullet points."),
])

# 4. Build the chain: prompt -> model -> plain text
chain = prompt | llm | StrOutputParser()


def main():
    print("Hello from Langchain-course")
    topic = input("Enter a topic: ")
    result = chain.invoke({"topic": topic})
    print("\n" + result)

if __name__=="__main__":
    main()


