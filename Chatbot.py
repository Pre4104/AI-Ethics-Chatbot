# AI Ethics Chatbot (Gemini 3 Flash - New SDK)

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found. Check your .env file.")
    st.stop()

# Initialize client
client = genai.Client(api_key=api_key)

# UI setup
st.set_page_config(page_title="AI Ethics Chatbot")
st.title("🤖 AI Ethics Chatbot (Gemini 3 Flash)")
st.write("Ask me anything about AI ethics!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Input
user_input = st.chat_input("Type your question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            try:
                prompt = f"""
You are an AI ethics expert.

If the user input is a simple greeting (like "hi", "hello", "hey"):
→ Respond naturally and briefly, like a human assistant.
→ Do NOT give ethical analysis.

If the input is a real question or scenario:
→ Respond in this structured format:

### 🧠 Ethical Analysis
### ⚠️ Risks
### ✅ Recommendations
### 🚦 Risk Level (Low/Medium/High)

User Query: {user_input}
"""

                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt
                )

                ai_message = response.text

                st.markdown(ai_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_message
                })

            except Exception as e:
                st.error(f"Error: {e}")
