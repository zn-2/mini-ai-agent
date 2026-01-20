# Import libraries 
from langchain_openai import ChatOpenAI 
import os
from dotenv import load_dotenv


# Model 
load_dotenv(override=True)
github_token = os.getenv('GITHUB_TOKEN')
llm = ChatOpenAI(base_url="https://models.inference.ai.azure.com",
                 api_key=github_token,
                 model="gpt-4o-mini",
                 temperature=0)


# Function to return response content
def ask(query: str):
    response = llm.invoke(query)
    return response.content