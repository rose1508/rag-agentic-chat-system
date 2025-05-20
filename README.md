rag_agentic_chat_system/
│
├── app/                        
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── db.py
│
├── pipeline/                  
│   ├── __init__.py
│   ├── fetch_federal_data.py
│   ├── process_data.py
│
├── static/                    
│   └── index.html
│
              
├── requirements.txt           
├── README.md                
├── .gitignore                
└── .env                  







# RAG Agentic Chat System (FastAPI + Ollama + MySQL)

This is a fully async, agentic RAG chat system using:
- FastAPI backend
- Ollama (Qwen) as LLM
- Async MySQL for storing registry data
- Agentic tool-calling to answer queries
- Basic frontend UI

# Setup

1. Clone repo
2. Create `.env` file
3. Install dependencies:
```bash
pip install -r requirements.txt

Run the Data Pipeline--"python -m pipeline.process_data"
Start the FastAPI Server--"uvicorn app.main:app --reload"
Open in Browser--"Visit: http://localhost:8000"
