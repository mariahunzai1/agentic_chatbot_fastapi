# frontend.py

import streamlit as st
import requests
import time

# --- Page Setup ---
st.set_page_config(page_title="LangGraph AI Agent", layout="centered")

# --- Header Styling ---
st.markdown("""
    <style>
        .title {font-size: 40px; font-weight: 700; text-align: center; margin-top: 0;}
        .subheader {text-align: center; font-size: 18px; margin-bottom: 30px; color: #666;}
        .stTextArea textarea { font-size: 16px; }
        .stSelectbox, .stRadio, .stCheckbox { font-size: 16px; }
    </style>
    <div class="title">🤖 LangGraph AI Agent</div>
    <div class="subheader">Build, Customize & Talk with Smart AI Chatbots</div>
""", unsafe_allow_html=True)

# --- System Prompt ---
st.markdown("### 🧠 System Behavior")
system_prompt = st.text_area(
    "Describe how your agent should behave:",
    height=80,  # 👈 FIXED from 60 to 80
    placeholder="E.g. Act like a helpful medical assistant..."
)

# --- Provider & Model ---
st.markdown("---")
st.markdown("### 🧩 Model & Provider")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mistral-saba-24b"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("🌐 Choose a Provider:", ("Groq", "OpenAI"))

selected_model = st.selectbox(
    "📦 Choose a Model:",
    MODEL_NAMES_GROQ if provider == "Groq" else MODEL_NAMES_OPENAI
)

# --- Web Search ---
allow_web_search = st.checkbox("🔎 Enable Real-time Web Search")

# --- Query Box ---
st.markdown("---")
st.markdown("### 💬 Ask a Question")
user_query = st.text_area(
    "What's your query?",
    height=150,
    placeholder="Type your question here..."
)

# --- Backend URL ---
API_URL = "http://127.0.0.1:9999/chat"

# --- Ask Button ---
st.markdown("---")
if st.button("🚀 Ask the Agent"):
    if user_query.strip():
        with st.spinner("Thinking... 💭"):
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }

            try:
                response = requests.post(API_URL, json=payload)

                if response.status_code == 200:
                    response_data = response.json()
                    if "error" in response_data:
                        st.error(f"❌ {response_data['error']}")
                    else:
                        st.success("✅ Agent responded successfully!")
                        time.sleep(0.5)
                        st.markdown("### 🤖 Agent Response")
                        st.info(response_data.get("response", "No response received."))
                else:
                    st.error(f"⚠️ Server returned status code: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the backend. Is FastAPI running at http://127.0.0.1:9999?")
    else:
        st.warning("⚠️ Please type a question before clicking 'Ask the Agent'.")

# --- Footer ---
st.markdown("---")
st.markdown("<center>Made with ❤️ using LangGraph, Groq, and OpenAI</center>", unsafe_allow_html=True)
