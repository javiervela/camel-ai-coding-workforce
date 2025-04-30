# CAMEL-AI Coding Workforce

This repository implements a **Multi-Agent System** using the **CAMEL-AI** framework, where specialized **LLM-based agents** collaborate to generate, review, document, test, and evaluate code. It includes a **Streamlit interface** for task input, live logging, and result visualization.

## Features

- **Multi-Agent System**: A workforce of specialized agents, each with a unique role:
  - **Coder Agent**: Generates code based on user prompts.
  - **Code Reviewer Agent**: Reviews code and suggests improvements.
  - **Code Documenter Agent**: Creates documentation for the code.
  - **Code Tester Agent**: Generates and executes test cases.
  - **Code Evaluator Agent**: Scores code quality, test coverage, and documentation clarity.
- **Streamlit Interface**: A user-friendly web interface for:
  - Inputting tasks.
  - Viewing live logs during task execution.
  - Displaying task results and workforce logs.
- **Customizable Models**: Supports OpenAI GPT-4 and other models via the CAMEL-AI framework.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/javiervela/camel-ai-coding-workforce.git
   cd camel-ai-coding-workforce
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Set up environment variables: Create a `.env` file in the root directory and configure any necessary environment variables like `OPENAI_API_KEY`. For example:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   CAMEL_API_URL=http://localhost:8000
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   poetry run streamlit run src/camel_ai_coding_workforce/main.py
   ```
2. Open your web browser and navigate to `http://localhost:8501` to access the interface.
3. Enter your task in the input field and click "Run".

## Dependencies

- Python 3.12
- Poetry
- CAMEL-AI
- Streamlit
