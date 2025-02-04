import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from tools.query_based_transaction_fetcher import fetch_transaction_data
from langchain_core.tools import tool

# Ensure the images directory exists
IMAGE_DIR = "generated_charts"
os.makedirs(IMAGE_DIR, exist_ok=True)

@tool
def generate_pie_chart(user_query: str) -> str:
    """
    Generates a pie chart showing spending distribution by category.
    """

    # Step 1: Fetch transactions using the fetcher tool
    fetched_data = fetch_transaction_data.invoke({"user_query": user_query})

    print(fetched_data)

    # Handle errors
    if fetched_data.get("status") == "error":
        return f"❌ {fetched_data['message']}"

    transactions = fetched_data.get("data", [])

    # Step 2: Check if there is valid transaction data
    if not transactions:
        return "✅ No transactions found matching your request."

    # Step 3: Aggregate spending by category
    category_totals = {}
    for txn in transactions:
        category = txn["category"]
        amount = float(txn["amount"])  # Convert to float for calculation

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    # Step 4: Prepare data for plotting
    labels = list(category_totals.keys())
    values = list(category_totals.values())

    # Step 5: Generate the Pie Chart
    plt.figure(figsize=(12, 10))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Spending Breakdown by Category")

    # Step 6: Save the chart
    chart_path = os.path.join(IMAGE_DIR, "spending_pie_chart.png")
    plt.savefig(chart_path)
    plt.close()

    return f"✅ Pie Chart Generated: {chart_path}"


# ✅ Example Usage:
if __name__ == "__main__":
    print(generate_pie_chart.invoke({"user_query": "Show me a breakdown of my spending in January 2024."}))
