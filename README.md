# 🏦 Personal Finance Insights System 🚀

An AI-powered **Personal Finance Insights System** using **LangChain with Agentic RAG**, enabling **transaction analysis, summaries, and visualizations** through intelligent **agents and tools**.

## 📌 Features

✅ **Upload Transactions** via:
   - Plain text CSV  
   - File upload  
   - URL-based CSV retrieval  

✅ **Query Transactions**:
   - Get financial summaries 📜  
   - Fetch specific transaction details 🔍  
   - Generate graphs (Pie & Line Charts) 📊  

✅ **Uses Multi-Agent System**:
   - **Transaction Fetcher Agent** → Handles transaction ingestion  
   - **Transaction Query Agent** → Handles user queries & selects the right tool  

✅ **Data Storage & Processing**:
   - MySQL Database for transaction storage  
   - Flask Backend for API requests  
   - LangChain for AI-powered decision-making  

---

## 🏗️ System Architecture

The system is designed using **multi-agent collaboration**:
1. **Transaction Fetcher Agent** → Processes and stores transaction data.
2. **Transaction Query Agent** → Retrieves data and decides the appropriate tool.

**📌 Diagram:** *(Insert system architecture diagram here)*

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
      git clone https://github.com/aniruddha2004/personalFinanceInsightsSystem.git

### **2️⃣ Set Up a Virtual Environment**
      python -m venv myenv

### **3️⃣ Install Dependencies**
      pip install -r requirements.txt

### **4️⃣ Configure MySQL Database**
- Ensure MySQL is running.
- Create a database named `finance_db`.

### **5️⃣ Set Up Environment Variables**
Create a `.env` file and configure the required credentials, as mentioned in the`.env.example` file.

---

## 🏃 Running the Application

### **1️⃣ Start the Backend Server**
      python backend/app.py

### **4️⃣ Open the Frontend**
- Open the link in your browser.
- Upload a CSV file or enter transaction data.
- Query your financial insights.

---

## 📡 API Endpoints

| Endpoint        | Method | Description |
|----------------|--------|-------------|
| `/process`     | POST   | Upload transactions (CSV, text, or URL) |
| `/query`       | POST   | Query transactions for insights |
| `/`            | GET    | Open the upload page |

---

## 📊 How It Works?

### **1️⃣ Transaction Ingestion**
- User **uploads transactions** (text, file, or URL).
- **Transaction Fetcher Agent** stores the data in MySQL.

### **2️⃣ Query Processing**
- User asks a **financial query** (e.g., "What did I spend last month?").
- **Transaction Query Agent** selects the **correct tool** (summary, pie chart, or line chart).
- Data is retrieved from **MySQL** and formatted as needed.

### **3️⃣ Response Generation**
- **Summary Tool** → Generates a financial report.
- **Pie Chart Tool** → Shows category-wise spending.
- **Line Chart Tool** → Displays spending trends.

---

## 🛠️ Tech Stack

- **Backend** → Python, Flask
- **Frontend** → HTML, CSS, JavaScript
- **Database** → MySQL
- **AI/LLM** → LangChain + Ollama
- **Visualization** → Matplotlib

---

## 🔥 Future Enhancements
🚀 **Potential Improvements:**
- Integrate a **vector database** for smarter query retrieval.
- Improve LLM **decision-making** for better agent collaboration.
- Enhance **UI/UX** for a more seamless experience.

---

## 📞 Contact
💬 **For queries & discussions**:
- **Email**: [aniruddhag2004@gmail.com](mailto:aniruddhag2004@gmail.com)
- **LinkedIn**: [Aniruddha Ghosh](https://www.linkedin.com/in/aniruddha-ghosh-87428824b/)

---

🚀 **Star this repository if you like it!** ⭐  
