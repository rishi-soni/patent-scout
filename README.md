# 🔬 PatentScout

> Turn thousands of patents into one actionable insight.

An agentic AI that autonomously searches, parses, and analyzes biotech AI patents to identify **white spaces** — untapped innovation opportunities no one has claimed yet.

Built for the [Hackathon Name] hackathon.

---

## How It Works

```
You type a topic
    → Agent searches Google Patents
    → Agent parses the top results
    → Agent identifies white spaces
    → You get a report in seconds
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourname/patent-lens.git
cd patent-lens
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API keys
```bash
cp .env.example .env
```
Then edit `.env` and add:
- `ANTHROPIC_API_KEY` → [console.anthropic.com](https://console.anthropic.com)
- `SERPAPI_API_KEY` → [serpapi.com](https://serpapi.com) (100 free searches/month)

> **No API keys?** Mock data is built in — the agent still runs for testing.

---

## Run It

**Option A — Web UI (recommended for demo)**
```bash
streamlit run app.py
```
Then open [http://localhost:8501](http://localhost:8501)

**Option B — Terminal**
```bash
python main.py
```

---

## Project Structure

```
patent-lens/
├── app.py            # Streamlit UI
├── main.py           # Terminal entry point
├── agent/
│   └── agent.py      # AgentExecutor — connects LLM + tools
├── tools/
│   ├── search.py     # Searches Google Patents via SerpAPI
│   ├── parse.py      # Parses patent pages
│   └── summarize.py  # Identifies white spaces using Claude
├── requirements.txt
└── .env.example
```

---

## Tech Stack

| Layer | Tool |
|-------|------|
| LLM | Claude (Anthropic) |
| Agent Framework | LangChain |
| Patent Data | SerpAPI + Google Patents |
| Parsing | BeautifulSoup |
| UI | Streamlit |

---

## Example Output

```
## Landscape Summary
Heavy patent concentration in protein folding and genomic classification,
led by DeepMind, Illumina, and Insilico Medicine.

## White Spaces
1. AI for rare pediatric disease diagnostics — fewer than 12 patents globally
2. Reinforcement learning for antimicrobial resistance prediction
3. Multimodal AI combining genomics + imaging for early cancer detection

## Recommended Next Steps
- File provisional patents in rare disease diagnostics
- Conduct prior art search in antimicrobial RL applications
```
