# DeepSeek Code Companion

🚀 Your AI Pair Programmer with Debugging Superpowers

## Overview
The **DeepSeek Code Companion** is a Streamlit-based chatbot application powered by Ollama and LangChain. It acts as an AI coding assistant, providing support for debugging, code documentation, solution design, and more. The application is designed to help developers write better code faster by leveraging AI capabilities.

## Features
- 🐍 **Python Expert**: Get expert-level assistance with Python programming.
- 🐞 **Debugging Assistant**: Identify and fix bugs in your code with strategic debugging suggestions.
- 📝 **Code Documentation**: Automatically generate clear and concise documentation for your code.
- 💡 **Solution Design**: Receive well-structured solutions for complex coding problems.

---

## Project Structure

deepseek-chatbot/
│
├── app.py                # Main application entry point
├── style.py              # Custom CSS styles
├── utils/                # Utility functions and helpers
│   └── chat_utils.py     # Chat-related utility functions
├── services/             # Service layer for business logic
│   └── chat_service.py   # Handles chat interactions and AI responses
├── README.md             # Project documentation



## How to Run
1. Install dependencies:
   ```bash
   pip install streamlit langchain-ollama langchain-core
   ```
2. Run the following command
   ```bash
   streamlit run app.py
   ```

---

### **Key Improvements**
1. **Modularity**: Separated concerns into `utils` and `services` for better maintainability.
2. **Documentation**: Added docstrings and comments to explain the purpose of each function and class.
3. **Scalability**: The structure allows for easy addition of new features or models.
4. **Readability**: Improved code organization and naming conventions.

Let me know if you need further assistance! 🚀
# deepseek-chatbot
# deepseek-chatbot
