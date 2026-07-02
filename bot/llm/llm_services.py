import os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from .prompt import system_message,context_text
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()

chat_llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",   
    temperature=0.7,
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

