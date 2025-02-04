import requests
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from langchain_core.tools import tool
from tools.csv_processing_tool import process_csv_file  # Importing the CSV Processor

@tool
def fetch_and_process_csv(url: str) -> str:
    """Downloads a CSV file from a given URL, saves it, and processes it."""
    file_name = "downloaded_transactions.csv"  # Save all downloads with this name
    file_path = os.path.join(os.getcwd(), file_name)

    try:
        # Download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error if the request fails

        # Save the file locally
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        # Process the downloaded file
        processed_result = process_csv_file.invoke({"file_path": file_path})

        # Check if the response is a string or structured data
        if isinstance(processed_result, str):
            # Handle plain string response
            return f"❌ Error: {processed_result}"
        elif isinstance(processed_result, dict):
            # Process structured response
            if processed_result.get("status") == "success":
                for transaction in processed_result.get("data", []):
                    # Wrap each transaction in `input_data`
                    wrapped_result = store_transaction.invoke({"input_data": transaction})
                    print(f"Processed transaction: {transaction}, Result: {wrapped_result}")
                return "✅ All transactions processed and stored successfully."
            else:
                return f"❌ Error processing CSV: {processed_result.get('message', 'Unknown error')}"

    except requests.exceptions.RequestException as e:
        return f"❌ Error downloading file: {e}"

    except Exception as e:
        return f"❌ Error processing file: {e}"


# ✅ Example Usage:
if __name__ == "__main__":
    csv_url = "https://raw.githubusercontent.com/aniruddha2004/test/refs/heads/main/sample_transactions.csv?token=GHSAT0AAAAAAC45TKBDNLA5SQLZUQ57BE7EZ43QYYA"  # Sample CSV URL
    print(fetch_and_process_csv.invoke({"url": csv_url}))
