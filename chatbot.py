# import streamlit as st
# import os
# from openai import OpenAI

# client = OpenAI(
#     api_key=os.environ.get("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1",
# )

# model="openai/gpt-oss-20b"

# SYSTEM_PROMPT = """
# You are a friendly, intelligent, professional, and helpful AI assistant.

# Your main goal is to understand users' questions and provide accurate, clear, useful, and easy-to-understand answers.

# Language Rules:
# - If the user speaks in Roman Urdu, always reply in Roman Urdu.
# - If the user speaks in English, reply in English.
# - Never use Hindi or Devanagari script.
# - Match the user's language and communication style.

# Behavior:
# - Always be polite, respectful, friendly, and supportive.
# - Understand the user's intent before answering.
# - Give direct and relevant answers without unnecessary details.
# - Explain complicated topics in simple words.
# - If the question is unclear, ask a short clarification question.
# - Never make up facts or provide misleading information.
# - If you don't know something, honestly say so.
# - Provide examples when they help explain something.
# - Follow the user's instructions carefully.
# - Keep conversations natural and engaging.
# - Avoid repeating the same information unnecessarily.

# Problem Solving:
# - Think carefully before answering.
# - Break complex problems into simple steps.
# - Provide practical solutions whenever possible.
# - For technical questions, provide accurate explanations and working code when appropriate.

# Your priority is to make every interaction helpful, accurate, natural, and enjoyable.
# """
# st.title("Mera Chatbot")
# st.caption("Ask me anything!")

# if "message" not in st.session_state:
#     st.session_state.message = [{
#         "role": "system",
#         "content": SYSTEM_PROMPT
#     }]

# # Clear chat history button
# if st.button("Clear Chat History"):
#     st.session_state.message = [{
#         "role": "system",
#         "content": SYSTEM_PROMPT
#     }]
#     st.rerun()

# #Display chat messages from history on app rerun
#     for msg in st.session_state.message:
#         if msg["role"] != "system":
#             st.write(msg["content"])

# #User input
# if prompt := st.text_input("Apna sawal yahan likhein:"):

#    # Displya User Message
#    with st.chat_message("user"):
#        st.write(prompt)

#        st.session_state.message.append({
#            "role": "user",
#             "content": prompt
#          })

# #generate AI response

#    with st.chat_message("assistant"):
#         with st.spinner("Soch raha hoon..."):
#             try:
#                 response = client.chat.completions.create(
#                     model=model,
#                     messages=st.session_state.message,
#                 )

#                 reply = response.choices[0].message.content

#             except Exception as e:
#                     reply = f"Error: {str(e)}"

#         st.write(reply)

#     #Save assistant response to session state
#         st.session_state.message.append({
#             "role": "assistant",
#             "content": reply
#         })
                


import streamlit as st
import os
from openai import OpenAI

# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }

    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        color: #58a6ff;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #aab4c3;
        font-size: 15px;
        margin-bottom: 30px;
    }

    [data-testid="stChatMessage"] {
        border-radius: 12px;
        padding: 12px;
    }

    .stButton button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }

    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)


# ==============================
# OPENAI / GROQ CONFIGURATION
# ==============================

API_KEY = os.environ.get("GROQ_API_KEY")


MODEL = "openai/gpt-oss-20b"

if not API_KEY:
    st.error("GROQ_API_KEY environment variable is missing!")
    st.info("Please configure your Groq API key and restart the app.")
    st.stop()

client = OpenAI(
    api_key=API_KEY,
    # api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
    timeout=60.0
)


# ==============================
# SYSTEM PROMPT
# ==============================

SYSTEM_PROMPT = """
You are a friendly, intelligent, professional, and helpful AI assistant.

Your goal is to understand users and provide accurate, useful,
clear, and easy-to-understand answers.

LANGUAGE RULES:
- If the user speaks Roman Urdu, reply in Roman Urdu.
- If the user speaks English, reply in English.
- Never use Hindi or Devanagari script.
- Match the user's language and communication style.

BEHAVIOR:
- Always be polite, friendly, and respectful.
- Understand the user's question before answering.
- Give direct and relevant answers.
- Explain complicated topics in simple words.
- Never invent facts or provide misleading information.
- If you don't know something, say so honestly.
- Ask clarification questions when necessary.
- Avoid unnecessary repetition.

PROBLEM SOLVING:
- Think carefully before answering.
- Explain solutions step by step when needed.
- Provide practical examples.
- For programming questions, provide clean and working code.

Your priority is to make every interaction helpful,
accurate, natural, and enjoyable.
"""


# ==============================
# SESSION STATE
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="main-title">🤖 My AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Your Smart AI Assistant | Ask Anything!</div>',
    unsafe_allow_html=True
)

st.divider()


# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("### 🤖 About Assistant")
    st.write(
        "Your personal AI assistant powered by "
        "Groq and OpenAI-compatible API."
    )

    st.divider()


    if st.button("🗑️ Clear Chat History"):

        st.session_state.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        st.rerun()

    st.caption("Made with ❤️ Coding by ( Waleed ) using Streamlit")


# ==============================
# DISPLAY CHAT HISTORY
# ==============================

for msg in st.session_state.messages:

    if msg["role"] == "system":
        continue

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


# ==============================
# USER INPUT
# ==============================

prompt = st.chat_input("Apna sawal yahan likhein... 💬")


# ==============================
# GENERATE AI RESPONSE
# ==============================

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("🤔 AI soch raha hai..."):

            try:

                response = client.chat.completions.create(
                    model=MODEL,
                    messages=st.session_state.messages
                )

                reply = response.choices[0].message.content

                if not reply:
                    reply = "Sorry, mujhe koi response nahi mila."

            except Exception as e:

                reply = f"❌ Error: {str(e)}"

        st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
