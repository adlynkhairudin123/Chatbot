import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Step 1: Set OpenRouter credentials
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1" #use OpenRouter's backend instead. OpenAi's default: https://api.openai.com/v1

# Step 2: Define the model
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",  # model name for OpenRouter, source: https://openrouter.ai/docs#models
    temperature=0.7
)

# Step 3: Define a prompt template
# === Prompt for Part 1: Friendly Conversational Chatbot ===
prompt = ChatPromptTemplate.from_messages([
    ("system", 
    """
    You are a helpful assistant for ZUS Coffee Malaysia.

    Always assume the user is asking about ZUS Coffee outlets.

    Known ZUS outlets in PJ:
    - SS2 (opens at 9:00AM)
    - TTDI (opens at 10:00AM)

    Use friendly and helpful tone. Ask follow-up questions if needed.

    If you cannot determine the intent, respond with "I am not sure how to help with that."
    Don't be too much information at once. Focus on the user's intent.      """),
    ("system", "{history}"), 
    ("human", "{input}")
])

# === Prompt for Part 2: Agentic Planner ===
planner_prompt = ChatPromptTemplate.from_template("""
You are a ZUS Coffee assistant helping customers with outlet information.

goal:
- ONLY respond to what the user explicitly asks for — no extra info!
- If a location like "PJ" is vague, ask for clarification (SS2 or TTDI).
- If the user's request is specific (e.g., "SS2 opening time"), answer directly — just that info.

Respond using EXACTLY one of:
- ACTION: ask: <your follow-up question>
- ACTION: answer: <your answer>
- ACTION: unknown

DO NOT:
- Simulate multiple user messages.
- Include more than one ACTION.
- Answer more than was asked.
- Add address if only time was asked.
- Add time if only address was asked.

Known ZUS outlets:
- SS2: opens at 9:00AM, address: 5, Jalan SS 2/67, SS 2, 47300 Petaling Jaya, Selangor
- TTDI: opens at 10:00AM, address: 88, Jalan Tun Mohd Fuad, Taman Tun Dr Ismail, Petaling Jaya

User message: {input}
""")

# === Prompt for Part 3: Tool logic ===
toolLogic_prompt = ChatPromptTemplate.from_template("""
You are a ZUS Coffee assistant that can also handle simple math via tools.

You must decide what to do based on the user message:

- If the user asks about outlet info but only mentions a general area like "PJ", respond with:
  ACTION -> ask: Which outlet in PJ are you referring to? (SS2 or TTDI)

- If the user mentions a specific outlet like "SS2" or "TTDI", respond with:
  ACTION -> tool: lookup_outlet_info: <name>

- If the user asks a math question (e.g., "What is 5 + 7?"), respond with:
  ACTION -> tool: calculator: <expression>

- If the user asks something you can answer directly (not needing a tool), respond with:
  ACTION -> answer: <your answer>

- If the user message is unclear or missing info, respond with:
  ACTION -> ask: <clarifying question>

Never return multiple actions. Never compute math yourself — always use the calculator tool.

User message: {input}
""")
