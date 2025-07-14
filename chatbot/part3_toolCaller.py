from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from config import llm, toolLogic_prompt
from tool_router import route_tool_call

# --- Chain: prompt → llm → output parser ---
planner_chain = toolLogic_prompt | llm | StrOutputParser()

# --- Controller ---
def controller(action_string: str):
    action_string = action_string.strip()

    if action_string.startswith("ACTION -> ask:"):
        q = action_string.replace("ACTION -> ask:", "").strip()
        return f"🤔 {q}"

    elif action_string.startswith("ACTION -> answer:"):
        ans = action_string.replace("ACTION -> answer:", "").strip()
        return f"✅ {ans}"

    elif action_string.startswith("ACTION -> tool:"):
        tool_info = action_string.replace("ACTION -> tool:", "").strip()
        result = route_tool_call(tool_info)
        return f"🛠️ [Tool Call Result]: {result}"

    # 🛠️ Handle misformatted tool call (fallback logic)
    elif "lookup_outlet_info" in action_string:
        return f"🛠️ [Tool Call Detected] But format incorrect → {action_string}"

    else:
        return "❌ (Planner failed to parse intent.)"

# --- Final controller chain ---
controller_chain = planner_chain | RunnableLambda(controller)

# --- Run in terminal ---
if __name__ == "__main__":
    print("Tool Calling Chatbot (Part 3). Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        raw = planner_chain.invoke({"input": user_input})
        print("\nRaw planner output:", repr(raw))

        response = controller(raw)
        print("Bot:", response)
