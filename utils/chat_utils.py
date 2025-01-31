import streamlit as st 
def initialize_session_state():
    """
    Initialize the session state for storing chat messages.
    """
    if "message_log" not in st.session_state:
        st.session_state.message_log = [
            {"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}
        ]

def display_chat_messages():
    """
    Display chat messages in the chat container.
    """
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.message_log:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])