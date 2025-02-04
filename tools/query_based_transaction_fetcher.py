import mysql.connector
from langchain_ollama.chat_models import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Ollama LLM
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
)

# Establish database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password=os.getenv('MYSQL_PASSWORD'),  # Replace with your MySQL password
    database="finance_db"
)

mycursor = mydb.cursor()

@tool
def fetch_transaction_data(user_query: str) -> dict:
    """
    Generates an SQL query using LLM, fetches transaction data, and returns structured JSON.
    """

    # Step 1: Generate SQL query using the LLM
    system_prompt = (
        "You are an AI that generates MySQL queries based on user input.\n"
        "The database has a table `transactions` with columns:\n"
        "- `date`: DATE\n"
        "- `description`: VARCHAR\n"
        "- `amount`: DECIMAL\n"
        "- `category`: VARCHAR\n\n"
        "Generate only the SQL query in a single line. Also make sure that the column names are not changed, like if the sum of all amounts grouped by category is being calculated then that column name should also be amount, not anything else."
        "This is right :  SELECT category, SUM(amount) AS amount FROM transactions GROUP BY category;"
        "This is wrong :  SELECT category, SUM(amount) AS total FROM transactions GROUP BY category; as here the column name is being changed"
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_query)
    ]

    sql_query = llm.invoke(messages).content.strip()

    print(f"\nDEBUG: Generated SQL Query → {sql_query}\n")  # Debug SQL Query

    try:
        # Step 2: Execute SQL query
        mycursor.execute(sql_query)
        result = mycursor.fetchall()

        # Step 3: Fetch the column names dynamically
        column_names = [desc[0] for desc in mycursor.description]
        print(f"\nDEBUG: Column Names → {column_names}\n")  # Debug Column Names
        print(f"\nDEBUG: Raw Database Result → {result}\n")  # Debug SQL Result

        # Step 4: Check if result is empty
        if not result:
            return {"status": "success", "data": []}

        # Step 5: Convert result to structured format dynamically
        structured_result = []
        for row in result:
            row_dict = {column_names[i]: row[i] for i in range(len(row))}
            # Convert date and decimal types to string & float
            if "date" in row_dict and isinstance(row_dict["date"], datetime.date):
                row_dict["date"] = row_dict["date"].strftime("%Y-%m-%d")
            if "amount" in row_dict and isinstance(row_dict["amount"], (float, int)):
                row_dict["amount"] = float(row_dict["amount"])

            structured_result.append(row_dict)

        return {"status": "success", "data": structured_result}

    except mysql.connector.Error as e:
        return {"status": "error", "message": f"Database Error: {e}"}
    except Exception as e:
        return {"status": "error", "message": f"Error: {e}"}



# ✅ Example Usage:
if __name__ == "__main__":
    print(fetch_transaction_data.invoke({"user_query": "What are all my transactions in January 2024"}))
