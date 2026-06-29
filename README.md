# 🔬 PatentScout

> Turn thousands of patents into one actionable insight.

An agentic AI that autonomously searches, parses, and analyzes US biotech AI patents to identify **white spaces** — untapped innovation opportunities no one has claimed yet.

Built for a student hackathon. Fully free to run.

---

## The Problem

The biotech AI patent landscape contains thousands of complex documents that are impossible to manually analyze at scale. Companies miss untapped innovation opportunities because they can't efficiently identify what's already been claimed. PatentLens automates that entire process, turning raw patent data into actionable competitive intelligence in minutes.

---

## How It Works

```
You type a topic
    → Agent searches USPTO (free, no key needed)
    → Agent parses the top results
    → Agent identifies white spaces using Claude
    → You get a report in seconds
```

The agent is autonomous — it decides what to search, which patents to parse, and how to synthesize the findings. You just ask the question.

---

## Tech Stack

| Layer | Tool | Cost |
|-------|------|------|
| LLM + reasoning | Claude (Anthropic) | $5 free credit on signup |
| Agent framework | LangChain | Free / open source |
| Patent data | USPTO PatentsView API | Free, no key needed |
| Patent parsing | BeautifulSoup | Free / open source |
| UI | Streamlit | Free |
| Hosting | Run locally | Free |

**Only one API key required: Anthropic.**

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

### 3. Add your Anthropic API key
```bash
cp .env.example .env
```
Edit `.env` and add:
```
ANTHROPIC_API_KEY=your-key-here
```
Get your key at [console.anthropic.com](https://console.anthropic.com)
> **No key yet?** Mock data is built in — the agent still runs for testing.

---

## Run It

**Option A — Web UI (recommended for demo)**
```bash
streamlit run app.py
```
Opens at [http://localhost:8501](http://localhost:8501)

**Option B — Terminal**
```bash
python main.py
```

---

## Project Structure

```
patent-lens/
├── app.py               # Streamlit UI — your demo interface
├── main.py              # Terminal entry point
├── agent/
│   └── agent.py         # AgentExecutor — connects LLM + tools
├── tools/
│   ├── search.py        # Searches USPTO PatentsView API (free, no key)
│   ├── parse.py         # Parses patent pages with BeautifulSoup
│   └── summarize.py     # Identifies white spaces using Claude
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Example Output

```
## Landscape Summary
Heavy patent concentration in protein folding and genomic variant
classification, led by DeepMind, Illumina, and Insilico Medicine.
AI-assisted drug discovery accounts for 60% of filings since 2020.

## Key Players
- DeepMind: protein structure prediction
- Illumina: genomic sequencing + classification
- Insilico Medicine: generative molecule design

## Crowded Areas (Already Claimed)
- AI-assisted protein folding
- Genomic variant classification
- Neural networks for medical imaging

## White Spaces (Top 3 Opportunities)
1. AI for rare pediatric disease diagnostics — fewer than 12 patents globally
2. Reinforcement learning for antimicrobial resistance prediction
3. Multimodal AI combining genomics + imaging for early cancer detection

## Recommended Next Steps
- Conduct prior art search in rare disease diagnostics
- File provisional patent in antimicrobial RL space
- Explore partnerships with academic medical centers
```

---

## Cost

| Item | Cost |
|------|------|
| USPTO PatentsView API | Free, unlimited |
| Anthropic API | ~$0.03–0.05 per full agent run |
| Everything else | Free |


---