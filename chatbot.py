import streamlit as st
import os
from openai import OpenAI

# Groq API Client
client = OpenAI(
    # api_key=os.environ.get("GROQ_KEYS"),
     api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-20b"

SYSTEM_PROMPT = """
You are a friendly, intelligent, professional, and helpful AI assistant.

Your main goal is to understand users' questions and provide accurate,
clear, useful, and easy-to-understand answers.

Language Rules:
- If the user speaks in Roman Urdu, always reply in Roman Urdu.
- If the user speaks in English, reply in English.
- Never use Hindi or Devanagari script.
- Match the user's language and communication style.

Behavior:
- Always be polite, respectful, friendly, and supportive.
- Understand the user's intent before answering.
- Give direct and relevant answers without unnecessary details.
- Explain complicated topics in simple words.
- If the question is unclear, ask a short clarification question.
- Never make up facts or provide misleading information.
- If you don't know something, honestly say so.
- Provide examples when they help explain something.
- Follow the user's instructions carefully.
- Keep conversations natural and engaging.

Problem Solving:
- Think carefully before answering.
- Break complex topics into simple steps.
- Provide practical solutions whenever possible.
"""


st.title("CHATBOT")
st.caption("Powered by Groq API")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# Clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    st.rerun()

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# User input
if prompt := st.chat_input("Apna sawal likhain..."):

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=st.session_state.messages
                )

                reply = response.choices[0].message.content

            except Exception as e:
                reply = f"Error: {str(e)}"

        st.write(reply)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })