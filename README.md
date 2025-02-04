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
3. **LangChain Tools**:
   - **Summarization Tool** → Generates human-readable reports.
   - **Pie Chart Tool** → Category-wise expense breakdown.
   - **Line Chart Tool** → Time-based spending trends.

**📌 Diagram:** *(Insert system architecture diagram here)*

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**

### **2️⃣ Set Up a Virtual Environment**

### **3️⃣ Install Dependencies**

### **4️⃣ Configure MySQL Database**
- Ensure MySQL is running.
- Create a database and update `config.py` with your credentials.

### **5️⃣ Set Up Environment Variables**
Create a `.env` file and configure the required credentials.

---

## 🏃 Running the Application

### **1️⃣ Start the Backend Server**

### **2️⃣ Run Transaction Fetcher Agent**

### **3️⃣ Run Transaction Query Agent**

### **4️⃣ Open the Frontend**
- Open `index.html` in your browser.
- Upload a CSV file or enter transaction data.
- Query your financial insights.

---

## 📡 API Endpoints

| Endpoint        | Method | Description |
|----------------|--------|-------------|
| `/process`     | POST   | Upload transactions (CSV, text, or URL) |
| `/query`       | POST   | Query transactions for insights |
| `/`            | GET    | Open the upload page |

### **Example API Request**

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

## 📜 Sequence Diagrams

### **1️⃣ Transaction Fetcher Agent**
*(Insert sequence diagram here)*

### **2️⃣ Transaction Query Agent**
*(Insert sequence diagram here)*

### **3️⃣ Full System Flow**
*(Insert full system sequence diagram here)*

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

## 🤝 Contribution Guidelines
💡 Want to contribute? Follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit changes and push to your fork.
4. Create a Pull Request 🚀.

---

## 📝 License
This project is licensed under the **MIT License**.

---

## 💡 Acknowledgments
- **LangChain Documentation**
- **Matplotlib for Visualizations**
- **Flask & MySQL for Backend & Storage**
- **Inspiration from AI-powered financial tools**

---

## 📞 Contact
💬 **For queries & discussions**:
- **Email**: your@email.com
- **GitHub Issues**: Open an Issue.
- **LinkedIn**: Your Profile.

---

🚀 **Star this repository if you like it!** ⭐  
