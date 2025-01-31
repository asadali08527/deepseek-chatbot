from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

class ChatService:
    """
    Service class for handling chat interactions and generating AI responses.
    """
    def __init__(self, model: str):
        """
        Initialize the chat service with the selected model.
        
        Args:
            model (str): The model to use for generating responses.
        """
        self.llm_engine = ChatOllama(
            model=model,
            base_url="http://localhost:11434",
            temperature=0.3
        )
        self.system_prompt = SystemMessagePromptTemplate.from_template(
            "You are an expert AI coding assistant. Provide concise, correct solutions "
            "with strategic print statements for debugging. Always respond in English."
        )

    def generate_ai_response(self, message_log: list) -> str:
        """
        Generate an AI response based on the chat history.
        
        Args:
            message_log (list): The chat history containing user and AI messages.
        
        Returns:
            str: The AI-generated response.
        """
        prompt_chain = self._build_prompt_chain(message_log)
        processing_pipeline = prompt_chain | self.llm_engine | StrOutputParser()
        return processing_pipeline.invoke({})

    def _build_prompt_chain(self, message_log: list) -> ChatPromptTemplate:
        """
        Build the prompt chain for the AI based on the chat history.
        
        Args:
            message_log (list): The chat history containing user and AI messages.
        
        Returns:
            ChatPromptTemplate: The constructed prompt chain.
        """
        prompt_sequence = [self.system_prompt]
        for msg in message_log:
            if msg["role"] == "user":
                prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
            elif msg["role"] == "ai":
                prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
        return ChatPromptTemplate.from_messages(prompt_sequence)