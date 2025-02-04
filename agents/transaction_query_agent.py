import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_ollama.chat_models import ChatOllama
from tools.summarize_transaction_data import summarize_transaction_data
from tools.generate_pie_chart import generate_pie_chart
from tools.generate_line_chart import generate_line_chart
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

tools = [summarize_transaction_data, generate_pie_chart, generate_line_chart]

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "You are an intelligent financial assistant that analyzes user queries, retrieves transaction data, and selects the appropriate tool to generate insights.."
                "Available tools: summarize_transaction_data (generate financial summaries and return it to the user, dont send request to any other tools after this), "
                "generate_pie_chart (show category-wise spending), and generate_line_chart (track spending trends over time). "
                "Determine intent: Use summarize_transaction_data for summaries, generate_pie_chart for category breakdowns, and generate_line_chart for spending trends. "
                "If unclear, ask a clarifying question before proceeding. "
                "Fetch transaction data if needed, then process it with the correct tool and return either a text summary or a chart file path."),
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

# agent_executor.invoke({"input" : 'Give me a pie chart of my expenses for this month.'})
