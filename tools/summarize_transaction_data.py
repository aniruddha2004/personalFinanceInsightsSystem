import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_core.tools import tool
from langchain_ollama.chat_models import ChatOllama
from tools.query_based_transaction_fetcher import fetch_transaction_data
import json
from decimal import Decimal

# Initialize Ollama LLM
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
)

@tool
def summarize_transaction_data(user_query: str) -> str:
    """
    Uses an LLM to generate a human-readable financial summary based on the fetched transactions.
    
    Steps:
    1. Calls `fetch_transaction_data` to retrieve relevant transactions.
    2. Processes the fetched data and passes it to the LLM.
    3. Returns a well-structured financial summary.

    Parameters:
    - user_query (str): The user's natural language question.

    Returns:
    - str: A structured summary of the transactions.
    """

    # Step 1: Fetch transaction data based on the user query
    fetched_data = fetch_transaction_data.invoke({"user_query": user_query})

    # Handle errors from fetcher tool
    if fetched_data.get("status") == "error":
        return f"❌ {fetched_data['message']}"

    transactions = fetched_data.get("data", [])

    # Case 1: If it's a total spending query (single value result)
    if len(transactions) == 1 and "value" in transactions[0]:
        return f"✅ You have spent a total of **${transactions[0]['value']:.2f}**."

    # Case 2: If no transactions are found
    if not transactions:
        return "✅ No transactions found matching your request."

    # Convert transactions into a JSON string for LLM processing
    # transactions_json = json.dumps(transactions, indent=2)
    transactions_json = json.dumps(transactions, indent=2, default=lambda o: float(o) if isinstance(o, Decimal) else o)

    # Define system prompt for the LLM
    system_prompt = (
        "You are an AI financial assistant. Your task is to analyze transaction data "
        "and generate a detailed yet concise summary for the user.\n\n"
        "User Query: {user_query}\n\n"
        "Transaction Data:\n{transactions_json}\n\n"
        "Instructions:\n"
        "- Identify key spending trends.\n"
        "- Highlight total spending.\n"
        "- Identify the top spending category.\n"
        "- Identify the most expensive transaction if applicable.\n"
        "- Format the response in a structured, human-readable summary.\n"
        "- Do NOT return raw JSON. Convert it into a well-written summary. Strictly no code. Answers should be plain text."
    )

    # Pass input to LLM
    messages = [
        {"role": "system", "content": system_prompt.format(user_query=user_query, transactions_json=transactions_json)},
        {"role": "user", "content": "Generate a summary for the given transactions."}
    ]

    summary = llm.invoke(messages).content.strip()

    return summary

# ✅ Example Usage:
if __name__ == "__main__":
    print(summarize_transaction_data.invoke({"user_query": "What are all my spendings on uber?"}))
