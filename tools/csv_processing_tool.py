import csv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_core.tools import tool
from tools.database_tool import store_transaction  # Importing our database storage tool

@tool
def process_csv_file(file_path: str) -> str:
    """Parses a CSV file and stores transactions in the database."""
    if not os.path.exists(file_path):
        return "❌ Error: File not found."

    transactions_added = 0
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row if present
            
            for row in csv_reader:
                if len(row) < 4:  # Ensure at least 4 columns exist
                    continue
                date, description, amount, category = row[0], row[1], float(row[2]), row[3]

                # Wrap transaction inside `input_data`
                result = store_transaction.invoke({
                    "input_data": {  # This ensures proper validation
                        "date": date, 
                        "description": description, 
                        "amount": amount, 
                        "category": category
                    }
                })
                
                print(f"Processed transaction: {date}, {description}, {amount}, {category} → Result: {result}")
                transactions_added += 1

        return f"✅ {transactions_added} transactions processed and stored."

    except Exception as e:
        return f"❌ Error processing CSV: {e}"

# ✅ Example Usage:
if __name__ == "__main__":
    print(process_csv_file.invoke({"file_path": "C:/xampp/htdocs/personalFinanceInsightsSystem/downloaded_transactions.csv"}))
