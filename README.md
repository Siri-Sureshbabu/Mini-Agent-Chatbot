Mini Agent Chatbot (FastAPI)

 1. Project Overview
This project is a Mini Agent Chatbot built using FastAPI.  
The chatbot routes user questions to different tools based on the query type.
The agent supports:
- Weather lookup using static JSON data
- Document search using predefined documents
- Fallback response for irrelevant questions

This project demonstrates-basic agent logic, tool selection, and API design.


2. Selected Task
Task 3 – Mini Agent Chatbot with Tool Use


3. Architecture Summary
- FastAPI: Backend API service
- Agent Router: Decides which tool to use
- Weather Tool: Returns weather data from static JSON
- Document Search Tool: Keyword-based document retrieval
- Fallback Logic: Handles irrelevant queries
- SQLite: Stores chat logs and tool usage

Flow:
User Question → Agent Router → Tool Selection → Response


4. Setup Instructions
- Python Version: 3.9 or above
- Create Virtual Environment
   python -m venv aienv
- Activate environment:
  (Windows) aienv\Scripts\activate
  (Mac/Linux) source aienv/bin/activate
- Install dependencies: pip install -r requirements.txt
- Run API server: uvicorn app.main:app --reload
- Server URL: http://127.0.0.1:8000
- Swagger UI(API Testing): http://127.0.0.1:8000/docs
- API Endpints:
  POST /chat : Input- user question|| Output-Selected tool, Response, Retrieved contex
  GET /health: status code
- Environment Variables:
  No external APIs or environment variables are required.
  Weather data and documents are locally stored.
-Project Structure :
  Mini-Agent-Chatbot/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── weather.py
│   ├── search.py
│   └── db.py
│
├── data/
│   └── documents.txt
│
├── chat_logs.db
├── requirements.txt
├── setup.sh
├── README.md
└── test.py

- Agent Logic:
  If question relates to stored documents → vector search → LLM summarizes
  If question mentions weather or a city → return from JSON ● Otherwise → default LLM response

- Notes & Assumptions:
  This project focuses on agent routing logic,
  No frontend UI is required,
  Streamlit UI is optional and not included,
  Static data is used instead of real APIs,
  Code clarity is prioritized over extra features.

Tech Stack:
- Python
- FastAPI
- SQLite
