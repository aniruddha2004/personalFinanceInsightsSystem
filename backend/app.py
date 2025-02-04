import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from agents.transaction_fetcher_agent import agent_executor as fetcher_agent
from agents.transaction_query_agent import agent_executor as query_agent

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
CORS(app)

# Temporary directory for uploaded files
TEMP_DIR = "temp_files"
os.makedirs(TEMP_DIR, exist_ok=True)

# Serve the index.html file when accessing the root URL
@app.route("/")
def serve_upload_page():
    # Serve index.html from the frontend directory
    return send_from_directory("../frontend", "index.html")

### 🔹 Route 1: Process Transactions (First Agent)
@app.route("/process", methods=["POST"])
def process_transaction():
    if "input_data" in request.form:
        input_data = request.form["input_data"]
        result = fetcher_agent.invoke({"input": input_data})
        return jsonify({"message": result})

    elif "file" in request.files:
        file = request.files["file"]
        file_path = os.path.join(TEMP_DIR, file.filename)
        file.save(file_path)
        result = fetcher_agent.invoke({"input": file_path})
        return jsonify({"message": result})

    else:
        return jsonify({"error": "No input provided. Please enter text or upload a file."})


### 🔹 Route 2: Query Financial Insights (Second Agent)
@app.route("/query", methods=["POST"])
def query_transaction():
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "No query provided. Please enter a valid financial question."})

    user_query = data["query"]
    result = query_agent.invoke({"input": user_query})
    print(result)
    return jsonify({"message": result})


### 🔹 Home Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Transaction Processing Backend is Running"})

if __name__ == "__main__":
    app.run(debug=True)
