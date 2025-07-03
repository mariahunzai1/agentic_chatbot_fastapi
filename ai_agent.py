
# --- Step 0: Suppress LangChain warnings (optional) ---
import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

# --- Step 1: Load API keys ---
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Step 2: Import LLMs and Tools ---
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.messages.ai import AIMessage
from langgraph.prebuilt import create_react_agent

# --- Step 3: Define function to get AI response ---
def get_response_from_ai_agent(llm_id, query, allow_search=True, system_prompt="Act as an AI chatbot who is smart and friendly.", provider="Groq"):
    # Choose LLM based on provider
    if provider == 'Groq':
        llm = ChatGroq(model=llm_id)
    elif provider == 'OpenAI':
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError("Unsupported provider. Choose 'Groq' or 'OpenAI'.")

    # Select tools based on flag
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create the agent
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Define message state
    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=" ".join(query))
        ]
    }

    # Invoke the agent
    response = agent.invoke(state)

    # Extract only AI-generated messages
    messages = response.get("messages")
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response from agent."


# --- Step 4: Run standalone test (optional) ---
if __name__ == "__main__":
    answer = get_response_from_ai_agent(
        llm_id="llama3-70b-8192", 
        query="Tell me about the solar system", 
        allow_search=True,
        provider="Groq"
    )
    print(answer)

