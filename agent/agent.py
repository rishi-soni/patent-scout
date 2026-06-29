from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools.search import search_patents
from tools.parse import parse_patent
from tools.summarize import summarize_gap


def build_agent() -> AgentExecutor:
    llm = ChatAnthropic(
        model="claude-sonnet-4-6",
        temperature=0,
        max_tokens=4096
    )

    tools = [search_patents, parse_patent, summarize_gap]

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are PatentScout, a biotech patent intelligence agent.
         
Your job is to find WHITE SPACES — innovation areas not yet claimed in biotech AI patents.

Always follow this exact order:
1. Call search_patents to find relevant patents on the topic
2. Call parse_patent on the top 3-5 results
3. Call summarize_gap with all parsed patents to identify white spaces
4. Return a clear, structured final report to the user"""),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=10,
        handle_parsing_errors=True
    )
