import json
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage


@tool
def summarize_gap(patents_json: str) -> str:
    """
    Analyzes parsed patents and identifies white spaces — unclaimed innovation areas.
    Call this after parsing all relevant patents.
    Input: a JSON string containing a list of parsed patent objects.
    Returns a structured white space report.
    """
    llm = ChatAnthropic(model="claude-sonnet-4-6", temperature=0, max_tokens=2048)

    try:
        patents = json.loads(patents_json) if isinstance(patents_json, str) else patents_json
        if not isinstance(patents, list):
            patents = [patents]
    except Exception:
        patents = [{"raw": patents_json}]

    patent_text = ""
    for i, p in enumerate(patents, 1):
        patent_text += f"\n--- Patent {i} ---\n"
        if isinstance(p, dict):
            patent_text += f"Title: {p.get('title', 'Unknown')}\n"
            patent_text += f"Assignee: {p.get('assignee', 'Unknown')}\n"
            patent_text += f"Abstract: {p.get('abstract', '')}\n"
            claims = p.get("claims", [])
            if claims:
                patent_text += f"Key Claim: {claims[0]}\n"
        else:
            patent_text += str(p) + "\n"

    response = llm.invoke([
        SystemMessage(content="""You are a patent intelligence analyst specializing in biotech AI.
Analyze the provided patents and identify white spaces — specific areas of innovation that are NOT yet claimed.
Be concrete and specific. Ground every insight in the actual patents provided."""),

        HumanMessage(content=f"""Analyze these patents and produce a structured report:

{patent_text}

Format your response exactly like this:

## 🗺 Landscape Summary
[2-3 sentences on what's already heavily patented and by whom]

## 🏢 Key Players
[Who is filing and what they're focused on]

## ❌ Crowded Areas (Already Claimed)
[What's heavily patented — areas to avoid]

## ✅ White Spaces (Top 3 Opportunities)
[Specific unclaimed areas with explanation of why they matter]

## 🚀 Recommended Next Steps
[Concrete actions — what to research, build, or file]
""")
    ])

    return response.content
