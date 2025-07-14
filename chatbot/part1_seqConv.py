import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory

from config import llm, prompt  # shared config
from config import OPENAI_API_KEY, OPENAI_API_BASE  # loaded from .env

# Step 4: Wrap the model and prompt into a runnable
chain = prompt | llm

# Step 5: Add memory with message history
memory = ConversationBufferMemory(return_messages=True)

# Create a session id for this chat (fixed for now)
session_id = "test-session"

# Step 6: Wrap with message history support (v0.2+ style)
chain_with_memory = RunnableWithMessageHistory(
    chain,
    lambda session_id: memory.chat_memory,
    input_messages_key="input",
    history_messages_key="history"
)

# Step 7: Terminal loop
print("Chatbot with memory (OpenRouter). Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chain_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
    )
    print("Bot:", response.content)
