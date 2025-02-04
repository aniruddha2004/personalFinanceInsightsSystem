import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_ollama.chat_models import ChatOllama
from tools.database_tool import store_transaction
from tools.csv_processing_tool import process_csv_file
from tools.web_scraper_tool import fetch_and_process_csv
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor


llm = ChatOllama(
    model = "llama3.1",
    temperature = 0
)

# print(llm.invoke("Are you ready?"))

# print(store_transaction.invoke({"date": "2024-01-29", "description": "Amazon Purchase", "amount": 150.50, "category": "Shopping"}))

tools = [store_transaction, process_csv_file, fetch_and_process_csv]

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "You are a highly capable assistant designed to manage transaction data. "
                "You can process CSV files, store transaction data in a database, and fetch data from URLs. "
                "You must decide which tool to use based on the user's input: "
                "directly store data if the input is plain text CSV, process the file first in case of a file upload and then store, or use web scraper for a URL link, process file and then store the data. Always explain your actions clearly."
                "If directly the database tool is being called then a valid dictionary should be sent, not a stringified dictionary"
                "And there should be four keys amount, category, transport, description"
            ),
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

llm_with_tools = llm.bind_tools(tools)

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# agent_executor.invoke({"input" : '2024-01-30,Uber Ride,25.75,Transport'})
