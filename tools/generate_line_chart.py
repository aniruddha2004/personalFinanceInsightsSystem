import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from tools.query_based_transaction_fetcher import fetch_transaction_data
from langchain_core.tools import tool

# Ensure the images directory exists
IMAGE_DIR = "generated_charts"
os.makedirs(IMAGE_DIR, exist_ok=True)

@tool
def generate_line_chart(user_query: str) -> str:
    """
    Generates a line chart showing spending trends over time.
    """

    # Step 1: Fetch transactions using the fetcher tool
    fetched_data = fetch_transaction_data.invoke({"user_query": user_query})

    # Handle errors
    if fetched_data.get("status") == "error":
        return f"❌ {fetched_data['message']}"

    transactions = fetched_data.get("data", [])

    # Step 2: Validate transaction structure
    if not transactions:
        return "✅ No transactions found matching your request."

    # Step 3: Check the structure of the returned data
    if "date" not in transactions[0]:
        return "❌ Error: The fetched data does not contain date-based transactions."

    # Step 4: Aggregate spending by date
    spending_data = {}
    
    for txn in transactions:
        txn_date = txn["date"]
        amount = float(txn["amount"])  # Convert to float for calculations
        
        if txn_date in spending_data:
            spending_data[txn_date] += amount
        else:
            spending_data[txn_date] = amount

    # Step 5: Convert data to DataFrame for sorting
    df = pd.DataFrame(list(spending_data.items()), columns=["Date", "Amount"])
    df["Date"] = pd.to_datetime(df["Date"])  # Convert to datetime for proper plotting
    df = df.sort_values(by="Date")  # Ensure dates are in order

    # Step 6: Generate the Line Chart
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Amount"], marker="o", linestyle="-", color="b", linewidth=2)
    plt.xlabel("Date")
    plt.ylabel("Total Spending ($)")
    plt.title("Spending Trends Over Time")
    plt.xticks(rotation=45)
    plt.grid(True)

    # Step 7: Save the chart
    chart_path = os.path.join(IMAGE_DIR, "spending_line_chart.png")
    plt.savefig(chart_path)
    plt.close()

    return f"✅ Line Chart Generated: {chart_path}"
    

# ✅ Example Usage:
if __name__ == "__main__":
    print(generate_line_chart.invoke({"user_query": "Plot my daily expenses for January 2024"}))

