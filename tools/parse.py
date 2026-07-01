import json
import requests
from bs4 import BeautifulSoup
from langchain.tools import tool


@tool
def parse_patent(url: str) -> str:
    """
    Fetches and parses a patent page given its URL.
    Returns structured data: title, assignee, abstract, and claims.
    Call this on each relevant patent URL returned by search_patents.
    Input: a full patent URL.
    """
    if not url.startswith("http"):
        return "Invalid URL — must start with http."

    if "mock" in url:
        return _mock_parse(url)

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find(class_="invention-title") or soup.find("h1")
        title = title.get_text(strip=True) if title else "Unknown Title"

        abstract = soup.find(class_="abstract")
        # abstract = abstract.get_text(strip=True)[:1000] if abstract else "No abstract found"
        abstract = abstract.get_text(strip=True) if abstract else "No abstract found"

        # description = soup.find(class_="description")
        # description = description.get_text(strip=True) if description else "No description found"

        claims = []
        claims_section = soup.find(class_="claims")
        if claims_section:
            for c in claims_section.find_all("div", class_="claim")[:5]:
                claims.append(c.get_text(strip=True)[:300])

        res = json.dumps({
            "title": title,
            "abstract": abstract,
            "claims": claims,
            # "description": description,
            "url": url
        }, indent=2)

        # data = json.loads(res)
        # with open("output_pretty.json", "w") as file:
        #     json.dump(data, file, indent=4)
        return res

    except Exception as e:
        print(f"Parse error for {url}: {e} — using mock")
        return _mock_parse(url)


def _mock_parse(url: str) -> str:
    """Fallback mock parsed patent."""
    patent_id = url.split("/")[-1]
    return json.dumps({
        "title": f"Sample Biotech AI Patent ({patent_id})",
        "abstract": "A machine learning method applied to biological data for the purpose of identifying novel drug candidates and predicting therapeutic efficacy across multiple disease indications.",
        "claims": [
            "1. A computer-implemented method comprising: receiving biological sequence data; applying a neural network model to predict therapeutic targets...",
            "2. The method of claim 1, wherein the neural network comprises transformer-based attention layers trained on protein databases...",
        ],
        "url": url
    }, indent=2)
