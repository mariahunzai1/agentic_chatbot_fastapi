Agentic Chatbot (FastAPI + LangGraph)

A modular, intelligent chatbot framework built with **FastAPI**, **LangGraph**, and **Streamlit**, supporting dynamic language models from **Groq** and **OpenAI**, along with optional real-time web search using **Tavily**.

**Features:**

- Backend: FastAPI + LangGraph agent logic
- Frontend: Streamlit web UI
- Choose from multiple LLM providers (Groq, OpenAI)
- Optional web search tool (Tavily)
- Supports dynamic system prompts
- Fast & lightweight for local or cloud deployment

**Technologies Used:**

- Python 3.13
- FastAPI
- LangGraph + LangChain
- Streamlit
- Groq API / OpenAI API
- Tavily API (for search)
- Uvicorn
- Pydantic (data validation)
- Requests
- Pipenv (for dependency management)

**Project Structure:**

agentic_chatbot_fastapi/
│
├── .gitignore #hides files
├── Pipfile + Pipfile.lock # Pipenv dependencies
├── ai_agent.py # LangGraph agent setup
├── backend.py # FastAPI backend server
├── frontend.py # Streamlit user interface
└── README.md 

**Local Setup Instructions:**


1. Clone the Repo
git clone https://github.com/your-username/agentic_chatbot_fastapi.git
cd agentic_chatbot_fastapi

3. Create Virtual Environment & Install Dependencies
pip install pipenv
pipenv install

4. Create .env file
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
OPENAI_API_KEY=your_openai_key_here

**Running the App Locally:**

Step 1: Start FastAPI Backend
python backend.py

Step 2: Start Streamlit Frontend
streamlit run frontend.py

**Example Use Case:**
Example Prompt: "You are a friendly AI tutor. Help me understand Python lists."
Choose OpenAI → Groq
Ask: “How do Python lists work?”

**Author:** 
Maria Ali
 
