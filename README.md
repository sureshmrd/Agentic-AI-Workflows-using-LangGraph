# Agentic-Chatbot-WebSearch

An agentic, LangGraph-based chatbot with a Streamlit UI and a news-fetching/summarization node. The project combines a LangGraph workflow, a Groq LLM integration, and a news tool (Tavily) to fetch and summarize AI news into Markdown summaries stored in the `AINews/` folder.

**Highlights:**
- LangGraph-driven agent architecture (graph builder + nodes)
- Streamlit UI for quick interactive use
- `AINews` node uses Tavily to fetch news and an LLM to summarize
- Example news summaries saved under `AINews/{daily,weekly,monthly}_summary.md`

**Quick Start**
- Recommended: Python 3.10+ (project virtualenv uses Python 3.12)

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell
# or
.\.venv\Scripts\activate.bat  # cmd
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
# Option A: run as a normal Python script (calls the Streamlit UI loader)
python app.py

# Option B (recommended for Streamlit):
streamlit run app.py
```

**Where to look**
- App entry: `app.py` — calls `load_langgraph_agenticai_app()`
- Main app loader: `src/langgraphagenticai/main.py`
- UI: `src/langgraphagenticai/ui/streamlitui` (loads UI components)
- LLM adapters: `src/langgraphagenticai/LLMs` (e.g. `groq_llm.py`)
- Graph builder: `src/langgraphagenticai/graph/graph_builder.py`
- Nodes (tools): `src/langgraphagenticai/nodes` — includes `ai_news_node.py`
- News outputs: `AINews/` (contains generated markdown summaries)

**AI News node details**
- `src/langgraphagenticai/nodes/ai_news_node.py` uses `TavilyClient` to search news and an LLM prompt to produce markdown summaries.
- Summaries are written to `./AINews/{frequency}_summary.md` (e.g., `daily_summary.md`).

**Configuration / Environment**
- The project depends on external services (Tavily, any LLM endpoints). Ensure any required API keys / environment variables are set before running (e.g., Tavily credentials used by `TavilyClient`).
- If using GPU-backed vector stores or other providers, check the LLM adapter files in `src/langgraphagenticai/LLMs`.

**Development notes**
- To add new nodes or tools, implement them under `src/langgraphagenticai/nodes` and register/use them via the graph builder.
- Keep dependencies in `requirements.txt` up to date; tests and CI are not included in this repo snapshot.

**Troubleshooting**
- If Streamlit UI fails to appear, try `streamlit run app.py` from the project root.
- If news fetching fails, verify network access and Tavily credentials.
- If LLM initialization fails, inspect the adapter in `src/langgraphagenticai/LLMs/groq_llm.py` for required env vars or config.

**Project Structure (short)**

- `app.py` — script entry
- `requirements.txt` — Python deps
- `AINews/` — generated news summaries
- `src/langgraphagenticai/` — main package
  - `ui/streamlitui` — UI code
  - `LLMs/` — LLM adapters
  - `graph/` — graph builder logic
  - `nodes/` — nodes (e.g., `ai_news_node.py`)

**Next steps / suggestions**
- Add a `config.example.env` documenting any required API keys and env vars.
- Add a short CONTRIBUTING.md explaining how to extend nodes and graph use-cases.
- Add tests for node outputs and graph assembly.

**License**
- No license included. Add your preferred license file if you plan to share this repository.

---

_(README automatically created and summarizes files found in the repository.)_