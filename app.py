import streamlit as st
from services.chat_service import ChatService
from utils.chat_utils import initialize_session_state, display_chat_messages
from styles.style import style

# Custom CSS styling
st.markdown(style, unsafe_allow_html=True)

# App title and caption
st.title("🧠 DeepSeek Code Companion")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar configuration
def configure_sidebar():
    with st.sidebar:
        st.header("⚙️ Configuration")
        selected_model = st.selectbox(
            "Choose Model",
            ["deepseek-r1:1.5b", "deepseek-r1:70b"], # Pull Deepseek model locally by executing command ollama run deepseek-r1:1.5b
            index=1
        )
        st.divider()
        st.markdown("### Model Capabilities")
        st.markdown("""
        - 🐍 Python Expert
        - 🐞 Debugging Assistant
        - 📝 Code Documentation
        - 💡 Solution Design
        """)
        st.divider()
        st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")
    return selected_model

# Initialize session state
initialize_session_state()

# Display chat messages
display_chat_messages()

# Sidebar configuration and model selection
selected_model = configure_sidebar()

# Initialize chat service
chat_service = ChatService(model=selected_model)

# Chat input and processing
user_query = st.chat_input("Type your coding question here...")

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate AI response
    with st.spinner("🧠 Processing..."):
        ai_response = chat_service.generate_ai_response(st.session_state.message_log)
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Rerun to update chat display
    st.rerun()