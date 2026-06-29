from dotenv import load_dotenv
from agent.agent import build_agent

load_dotenv()

if __name__ == "__main__":
    agent = build_agent()
    query = "Find white spaces in biotech AI patents from 2020 to 2025"
    result = agent.invoke({"input": query})
    print(result["output"])
