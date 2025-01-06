#  Demo Bank Customer Support with with compliance guardrails



## Introduction

This project demonstrates how to build a reliable customer support bot using RAG (Retrieval Augmented Generation) for banking FAQs. The implementation features:

1.Streamlit-based interactive chat interface
2.LangChain for RAG capabilities
3.Built-in compliance guardrails for banking responses
4.Professional response validation
5.Source attribution for answers

## Architecture
Key system components:

RAG Engine: Document ingestion and query processing using LangChain and OpenAI
Guardrail System: Banking compliance checks and response validation
Streamlit Interface: Interactive web UI with chat functionality
Dataset: Banking FAQ knowledge base

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/multinear-demo/demo-bank-support-lc-py
    cd demo-bank-support-lc-py
    ```

2. **Configure Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

    ```bash
    echo "OPENAI_API_KEY=your-api-key-here" > .env
    ```

### Option 1: Using `uv` (Recommended)

   [`uv`](https://github.com/astral-sh/uv) is the fastest way to run the application with minimal setup.

```bash
# Setup Environment
uv sync

# Start the Application
uv run main.py
```

### Option 2: Using `pyenv`

   [`pyenv`](https://github.com/pyenv/pyenv) allows you to manage multiple Python versions and virtual environments.

```bash
# Setup Environment
pyenv install 3.9
pyenv virtualenv 3.9 demo-bank
pyenv local demo-bank
pip install -r requirements.txt

# Start the Application
python main.py
```

### Option 3: Using Python's built-in `venv`

```bash
# Setup Environment
python3 -m venv .venv
source .venv/bin/activate
# On Windows:
# .\.venv\Scripts\activate
pip install -r requirements.txt

# Start the Application
python3 main.py
```

Open http://127.0.0.1:8080 to see the application.

Try asking different questions to see how the bot handles them:

- Hi there!
- How do I reset my password?
- What's the current exchange rate?
- Where is the closest coffee shop?

## Tracing

Enable LLM tracing with [Arize Phoenix](https://phoenix.arize.com) in the `.env` file (see [.env.example](.env.example) and [tracing.py](tracing.py)).

---

### Jupyter Notebook

```bash
# Using uv
uv run --with jupyter jupyter lab notebook.ipynb

# Using pyenv / virtualenv
pip install jupyter
jupyter lab notebook.ipynb
```

## Architecture

   Key system components:

1. [RAG Engine](engine.py) for document ingestion, indexing, and query processing using the `LangChain` library and `OpenAI` model.
2. [API Server](api.py) with `FastAPI` endpoints for chat, reindexing, and session management.
3. [HTML](static/index.html) & [React JS](static/app.js) frontend.
4. [Dataset](data/acme_bank_faq.txt) for the RAG engine.
5. [Experiment Runner](.multinear/task_runner.py) entry point for `Multinear` platform.
6. [Configuration](.multinear/config.yaml) for evaluation tasks.

## Experimentation Platform

   The platform is designed to facilitate the development and evaluation of GenAI applications through systematic experimentation.

### Running Experiments

1. **Define Tasks**

   Configure your evaluation tasks in `.multinear/config.yaml`. Each task represents a specific input scenario for the customer support bot, and defines how to evaluate the output.

2. **Execute Experiments**

   Run `Multinear` platform.

    ```bash
    # Using uv
    uv run multinear web_dev

    # Using pyenv / virtualenv
    multinear web_dev
    ```

   Open http://127.0.0.1:8000 and start experimenting.

## License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
    <i>Built by <a href="https://multinear.com">Multinear</a>.</i>
</p>
