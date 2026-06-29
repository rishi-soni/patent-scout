import os
import json
import requests
from langchain.tools import tool


@tool
def search_patents(query: str) -> str:
    """
    Searches Google Patents for patents matching the query.
    Always call this first. Returns a list of patents with titles, URLs, assignees, and abstracts.
    Input: a search string like 'AI drug discovery 2022'.
    """
    api_key = os.getenv("SERPAPI_API_KEY")

    if not api_key:
        return _mock_results()

    try:
        params = {
            "engine": "google_patents",
            "q": query,
            "api_key": api_key,
            "num": 10,
        }
        response = requests.get("https://serpapi.com/search", params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        results = []
        for p in data.get("organic_results", [])[:10]:
            results.append({
                "title": p.get("title", "Unknown"),
                "url": p.get("patent_link", ""),
                "assignee": p.get("assignee", "Unknown"),
                "filing_date": p.get("filing_date", "Unknown"),
                "abstract": p.get("snippet", "No abstract available"),
            })
        return json.dumps(results, indent=2)

    except Exception as e:
        print(f"Search error: {e} — falling back to mock data")
        return _mock_results()


def _mock_results() -> str:
    """Fallback mock data when no API key is present or search fails."""
    return json.dumps([
        {
            "title": "AI-Assisted Protein Folding for Drug Target Identification",
            "url": "https://patents.google.com/patent/mock/US11111111",
            "assignee": "DeepMind Technologies",
            "filing_date": "2022-03-15",
            "abstract": "A transformer-based method to predict 3D protein structure for identifying drug binding sites."
        },
        {
            "title": "Machine Learning System for Genomic Variant Classification",
            "url": "https://patents.google.com/patent/mock/US22222222",
            "assignee": "Illumina Inc",
            "filing_date": "2021-07-20",
            "abstract": "Deep learning for classifying genomic variants associated with hereditary diseases."
        },
        {
            "title": "Reinforcement Learning for Novel Drug Molecule Generation",
            "url": "https://patents.google.com/patent/mock/US33333333",
            "assignee": "Insilico Medicine",
            "filing_date": "2023-01-10",
            "abstract": "RL agents generating novel molecular structures with desired pharmacological properties."
        },
        {
            "title": "NLP System for Clinical Trial Data Extraction",
            "url": "https://patents.google.com/patent/mock/US44444444",
            "assignee": "IBM Watson Health",
            "filing_date": "2020-09-05",
            "abstract": "Natural language processing pipeline for automated extraction of outcomes from clinical trial documents."
        },
        {
            "title": "Convolutional Neural Network for Medical Image Diagnosis",
            "url": "https://patents.google.com/patent/mock/US55555555",
            "assignee": "Google Health",
            "filing_date": "2021-11-30",
            "abstract": "CNN architecture for detecting anomalies in radiology images including CT scans and MRIs."
        },
    ], indent=2)
