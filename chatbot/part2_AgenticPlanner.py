import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_core.runnables import RunnableLambda 
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from config import llm, planner_prompt
from config import OPENAI_API_KEY, OPENAI_API_BASE  # Loads and sets env vars globally
from langchain_openai import ChatOpenAI

# === Planning logic ===
planner_chain = planner_prompt | llm | StrOutputParser()

# === Controller that processes action string ===
def controller(action_string: str):
    action_string = action_string.strip()  # Normalize whitespace
    normalized = action_string.lower().replace("->", ":").strip()

    if normalized.startswith("action: ask:"):
        follow_up = action_string.split("ask:")[-1].strip()
        return f"(Planner decided to ask more) : {follow_up}"

    elif normalized.startswith("action: answer:"):
        answer = action_string.split("answer:")[-1].strip()
        return f"(Planner answered directly) ✅: {answer}"

    elif normalized.startswith("action: tool:"):
        tool_instruction = action_string.split("tool:")[-1].strip()
        return f"(Planner decided to call a tool) 🛠️: [Simulated Tool Call] {tool_instruction}"

    elif "finish" in normalized:
        return "(Planner decided to end the conversation) "

    else:
        return "(Planner failed to parse intent.) ❌"

# === Chain the planner to controller ===
controller_chain = planner_chain | RunnableLambda(controller)

# === Run interactively ===
if __name__ == "__main__":
    print("Agentic Planner Chatbot (Part 2). Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        # Step 1: Run the planner to decide intent
        raw_output = planner_chain.invoke({"input": user_input})
        action_string = raw_output.strip()
        print("\nRaw planner output:", repr(action_string))  # Shows formatting issues

        # Step 2: Use controller to parse and respond
        response = controller(action_string)
        print("Bot:", response)
