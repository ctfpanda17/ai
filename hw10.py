import os
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq

os.environ["TAVILY_API_KEY"] = "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"

tools = [TavilySearchResults(max_results=1)]

# Get the prompt to use - you can modify this!
prompt = hub.pull("openai/web_semantic_scholar_instructions")

# Choose the LLM to use
llm = ChatGroq(api_key="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")

# Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

questions = input("questions:")
agent_executor.invoke({"input" : f"{questions} ?用中文回答"})