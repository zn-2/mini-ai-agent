# mini-ai-agent

📘 GitHub Models Agent 
This project calls a single LLM agent via Langchain and Github Models with a simple query via a custom ask() function that returns a response to the user.  

✨ Features
Straight forward structure

agent.py contains the LLM agent

main.py is used to call the agent with a query. 

Uses GitHub Models 

Custom ask() function for querying the model & returning a user friendly response. 


📂 Project Structure
Code
mini-ai-agent/
│
├── src/
│   ├── agent.py        # LLM & ask() function
│   ├── __init__.py
│
├── main.py             # Querying model
├── requirements.txt
└── .gitignore
🚀 Getting Started
Step 1 - Install all dependencies
Code
pip install -r requirements.txt
2. .env 
Create an .env file for your github token. 

Code
GITHUB_TOKEN=your_token_here
3. Run main.py (query script)
Code
python main.py
🧠 How It Works
The ask() function in src/agent.py:

loads your GitHub Models API key

initializes the model

sends a query

returns the model’s response

This keeps the interface simple and easy to understand.

The ask() function in src/agent.py: 

calls the initialised LLM model agent

receives the response

and returns it in a user friendly format 

📄 License
MIT
