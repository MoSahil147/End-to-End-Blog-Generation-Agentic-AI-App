# End-to-End Blog Generation Agentic AI App

This app generates blogs from a given topic using **Groq LLM** and **LangGraph**.  
Backend is built with **FastAPI**. You can use **Postman** or any REST client to test it.

---

## Setup Instructions

All commands must be run inside a virtual environment.

```bash
# 1️⃣ Create a virtual environment
python3 -m venv venv

# 2️⃣ Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
python app.py

# Use this to test LangGraph locally (must be inside venv)
langgraph dev