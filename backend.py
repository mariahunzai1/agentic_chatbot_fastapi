# backend.py

# Step 1: Pydantic schema for incoming request
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

# Step 2: Initialize FastAPI app
app = FastAPI(
    title="LangGraph AI Agent",
    description="An intelligent chatbot API using Groq/OpenAI + LangGraph + optional web search tools",
    version="1.0.0"
)

# Optional: Add a root route for friendliness
@app.get("/")
def read_root():
    return {"message": "Welcome to LangGraph AI Agent. Visit /docs to use the chatbot API."}

# Step 3: Allowed models
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "llama-3.3-70b-versatile",
    "mistral-saba-24b",
    "gpt-4o-mini"
]

# Step 4: Chat endpoint
@app.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        if request.model_name not in ALLOWED_MODEL_NAMES:
            return {"error": "Invalid model name. Kindly select a valid AI model."}

        response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )
        return {"response": response}
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": f"Internal error: {str(e)}"}


# Step 5: Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
