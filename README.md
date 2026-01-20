# mini-ai-agent

## 📘 GitHub Models Agent
This project calls a single LLM agent via LangChain and GitHub Models using a simple query through a custom `ask()` function that returns a response to the user.


## ✨ Features
- Straightforward structure

- `agent.py` contains the LLM agent

- `main.py` calls the agent with a query

- Uses GitHub Models

- Custom `ask()` function for querying the model and returning a user‑friendly response


## 📂 Project Structure
```python
mini-ai-agent/
│
├── src/
│   ├── agent.py      # LLM & ask() function
│   ├── __init__.py
│
├── main.py           # Querying the model
├── requirements.txt
└── .gitignore
```


## 🚀 Getting Started
**1. Install all dependencies**
```python
pip install -r requirements.txt
```
**2. Create a `.env` file**

Add your GitHub token here:
```python
GITHUB_TOKEN=your_token
```
**3. Run the query script**
```python
python main.py
```
**4. (Optional) Edit query & model**
- In `main.py` you can change the question sent to the model by updating the string.

- In `agent.py` you can change to any compatible GitHub model by updating the `model` parameter in the `ChatOpenAI` function.


## 🧠 How It Works
The `ask()` function in `src/agent.py`:

- loads your GitHub Models API key

- initializes the model

- sends a query

- receives the response

- returns it in a user‑friendly format


## 📄 License
MIT
