# mini-ai-agent

## GitHub Models Agent
This project calls a single LLM agent via LangChain and GitHub Models using a simple query through a custom ask() function that returns a response to the user.

## Features
Straightforward structure

agent.py contains the LLM agent

main.py calls the agent with a query

Uses GitHub Models

Custom ask() function for querying the model and returning a user‑friendly response

## Project Structure
Code
mini-ai-agent/
│
├── src/
│   ├── agent.py      # LLM & ask() function
│   ├── __init__.py
│
├── main.py           # Querying the model
├── requirements.txt
└── .gitignore

## Getting Started
1. Install dependencies
Code
pip install -r requirements.txt
2. Create a .env file
Code
GITHUB_TOKEN=your_token_here
3. Run the query script
Code
python main.py

## How It Works
The ask() function in src/agent.py:

loads your GitHub Models API key

initializes the model

sends a query

receives the response

returns it in a user‑friendly format

This keeps the interface simple and easy to understand.

## License
MIT
