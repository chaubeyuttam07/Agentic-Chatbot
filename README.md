# CHATBOT:🚀 LangGraph + AgenticAI + Groq + Streamlit

This project is a LangGraph-based LLM application that uses AgenticAI's capabilities and integrates with the Groq API to run fast, agent-based language tasks. A Streamlit interface is provided for user interaction and result visualization.

---

## 📦 Features

- ✅ LangGraph flow for managing agent steps.
- 🤖 Integration with `Groq` LLM models via `langchain_groq`.
- 🧠 Custom agent functions using LangChain tools.
- 🖼️ Interactive front-end using `Streamlit`.
- 📚 Modular design with clear separation of logic, graph construction, and UI.

---
## Future Impletation :
- Integrate to defferent other model
- Develop your own LLM model and integrate with it

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chaubeyuttam07/Agentic-Chatbot.git
   cd langgraph-Agentic_Chatbot
2. **Creating virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3.  Install dependencies

    ```bash
      pip install -r requirements.txt
4. Running the Application
    ```bash
      streamlit run app.py

Structure of file
 ```graphql
    .
├── src/
│   ├── app.py                      # Streamlit UI
│   ├── langgraphagenticai/
│   │   ├── user_controls.py        # Sidebar controls (API key, prompt, model)
│   │   ├── groq_llm.py             # Handles LLM creation with Groq
│   │   ├── graph_executor.py       # LangGraph setup and execution
│   │   ├── display_result.py       # Output rendering logic
│   │   └── graph_nodes/            # (Optional) Custom nodes/functions
├── requirements.txt
└── README.md


