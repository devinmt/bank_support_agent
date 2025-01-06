# Enhanced Bank Customer Support RAG with Streamlit

A RAG-powered banking customer support chatbot with compliance guardrails, built using Streamlit, LangChain, and OpenAI.

## Introduction

This project demonstrates how to build a reliable customer support bot using RAG (Retrieval Augmented Generation) for banking FAQs. The implementation features:

- Streamlit-based interactive chat interface
- LangChain for RAG capabilities
- Built-in compliance guardrails for banking responses
- Professional response validation
- Source attribution for answers

The <span style="color: red">key focus</span> is on **reliability** and **compliance** - ensuring the bot provides accurate answers while adhering to banking regulations and best practices.

## Architecture

Key system components:

1. [RAG Engine](engine.py): Document ingestion and query processing using LangChain and OpenAI
2. [Guardrail System](app.py): Banking compliance checks and response validation
3. [Streamlit Interface](app.py): Interactive web UI with chat functionality
4. [Dataset](data/acme_bank_faq.txt): Banking FAQ knowledge base

## Installation

1. **Clone the Repository**

```bash
git clone <https://github.com/devinmt/bank_support_agent.git>
cd <https://github.com/devinmt/bank_support_agent.git>
```

2. **Configure Environment Variables**

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your-api-key-here
```

### Option 1: Using `venv` (Recommended)

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the application
streamlit run app.py
```

### Option 2: Using `uv`

```bash
# Setup Environment
uv sync

# Start the Application
uv run -m streamlit run app.py
```

### Option 3: Using `pyenv`

```bash
# Setup Environment
pyenv install 3.9
pyenv virtualenv 3.9 bank-support
pyenv local bank-support
pip install -r requirements.txt

# Start the Application
streamlit run app.py
```

The application will be available at http://localhost:8501

## Example Questions

Try asking different questions to see how the bot handles them:

- "What are your operating hours?"
- "How do I reset my online banking password?"
- "Tell me about your mortgage rates"
- "What's the process for reporting fraud?"

## Features

1. **RAG Capabilities**
   - Document retrieval and ranking
   - Context-aware responses
   - Source attribution

2. **Banking Compliance**
   - Professional tone enforcement
   - Regulatory compliance checks
   - Sensitive information protection
   - Appropriate disclaimers

3. **User Interface**
   - Clean chat interface
   - Chat history management
   - Source references
   - Loading indicators

## Requirements

Main dependencies:
```
streamlit>=1.32.0
langchain>=0.3.8
langchain-openai>=0.2.10
langchain-community>=0.3.4
faiss-cpu>=1.9.0.post1
python-dotenv>=1.0.1
```

## License

This project is licensed under the MIT License.

---

<p align="center">
<i>Built with Streamlit and LangChain.</i>
</p>