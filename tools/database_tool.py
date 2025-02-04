import mysql.connector
from langchain_core.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

# Establish database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this to your MySQL username
    password=os.getenv('MYSQL_PASSWORD'),  # Change this to your MySQL password
    database="finance_db"
)

mycursor = mydb.cursor()

@tool
def store_transaction(input_data: dict) -> str:
    """
    Stores a transaction in the MySQL database.
    Handles both dictionary input and CSV string input formats.
    """
    # Validate the input_data format
    if not isinstance(input_data, dict):
        return "❌ Error: Invalid input format. Expected a dictionary."

    # Validate required keys in the input_data
    required_keys = {"date", "description", "amount", "category"}
    if not required_keys.issubset(input_data.keys()):
        return f"❌ Error: Missing required keys. Expected keys: {', '.join(required_keys)}."

    # Prepare SQL query and values
    sql = "INSERT INTO transactions (date, description, amount, category) VALUES (%s, %s, %s, %s)"
    val = (
        input_data["date"],
        input_data["description"],
        float(input_data["amount"]),  # Ensure amount is converted to float
        input_data["category"]
    )

    try:
        # Execute the query and commit the transaction
        mycursor.execute(sql, val)
        mydb.commit()
        return f"✅ {mycursor.rowcount} transaction inserted."
    except mysql.connector.Error as e:
        return f"❌ Database Error: {e}"


# ✅ Example Usage:
if __name__ == "__main__":
    # Using a dictionary (directly processed)
    print(store_transaction.invoke({"input_data": {"date": "2024-01-29", "description": "Amazon Purchase", "amount": 150.50, "category": "Shopping"}}))


    # Using a raw CSV string (converted to dictionary first)
    print(store_transaction.invoke({"input_data": {"date": "2024-01-30", "description": "Uber Ride", "amount": 25.75, "category": "Transport"}}))

