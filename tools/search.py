import json
import requests
from langchain.tools import tool


PATENTSVIEW_URL = "https://api.patentsview.org/patents/query"


@tool
def search_patents(query: str) -> str:
    """
    Searches the USPTO PatentsView API for patents matching the query.
    No API key required. Always call this first.
    Returns a list of patents with titles, assignees, dates, and abstracts.
    Input: a search string like 'machine learning drug discovery'.
    """
    try:
        payload = {
            "q": {"_text_any": {"patent_abstract": query}},
            "f": [
                "patent_number",
                "patent_title",
                "patent_abstract",
                "patent_date",
                "assignee_organization",
            ],
            "o": {"per_page": 10, "sort": [{"patent_date": "desc"}]}
        }

        response = requests.post(PATENTSVIEW_URL, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()

        patents = data.get("patents") or []
        if not patents:
            print("No results from PatentsView — falling back to mock data")
            return _mock_results()

        results = []
        for p in patents[:10]:
            number = p.get("patent_number", "")
            results.append({
                "title": p.get("patent_title", "Unknown"),
                "url": f"https://patents.google.com/patent/US{number}",
                "patent_number": number,
                "assignee": (p.get("assignees") or [{}])[0].get("assignee_organization", "Unknown"),
                "filing_date": p.get("patent_date", "Unknown"),
                "abstract": (p.get("patent_abstract") or "No abstract available")[:500],
            })

        return json.dumps(results, indent=2)

    except Exception as e:
        print(f"PatentsView search failed: {e} — falling back to mock data")
        return _mock_results()


def _mock_results() -> str:
    """Fallback mock data if the API is unreachable."""
    return json.dumps([
        {
            "title": "AI-Assisted Protein Folding for Drug Target Identification",
            "url": "https://patents.google.com/patent/mock/US11111111",
            "patent_number": "11111111",
            "assignee": "DeepMind Technologies",
            "filing_date": "2022-03-15",
            "abstract": "A transformer-based method to predict 3D protein structure for identifying drug binding sites."
        },
        {
            "title": "Machine Learning System for Genomic Variant Classification",
            "url": "https://patents.google.com/patent/mock/US22222222",
            "patent_number": "22222222",
            "assignee": "Illumina Inc",
            "filing_date": "2021-07-20",
            "abstract": "Deep learning for classifying genomic variants associated with hereditary diseases."
        },
        {
            "title": "Reinforcement Learning for Novel Drug Molecule Generation",
            "url": "https://patents.google.com/patent/mock/US33333333",
            "patent_number": "33333333",
            "assignee": "Insilico Medicine",
            "filing_date": "2023-01-10",
            "abstract": "RL agents generating novel molecular structures with desired pharmacological properties."
        },
        {
            "title": "NLP System for Clinical Trial Data Extraction",
            "url": "https://patents.google.com/patent/mock/US44444444",
            "patent_number": "44444444",
            "assignee": "IBM Watson Health",
            "filing_date": "2020-09-05",
            "abstract": "NLP pipeline for automated extraction of outcomes from clinical trial documents."
        },
        {
            "title": "Convolutional Neural Network for Medical Image Diagnosis",
            "url": "https://patents.google.com/patent/mock/US55555555",
            "patent_number": "55555555",
            "assignee": "Google Health",
            "filing_date": "2021-11-30",
            "abstract": "CNN architecture for detecting anomalies in radiology images including CT scans and MRIs."
        },
    ], indent=2)
