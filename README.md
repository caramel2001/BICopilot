# GenAI Insurance Tool

## Overview
The GenAI Insurance Tool is an advanced solution designed to transform natural language queries into precise SQL translations and generate insights from Tableau dashboards. It leverages Microsoft's Autogen library to create agentic flows, using OpenAI or Llama models as the backend LLMs.

## Project Structure
```
genai-insurance-tool/
├── README.md
├── LICENSE
├── .gitignore
├── config/
│   ├── database.yml
│   ├── llm_config.yml
│   ├── tableau_api.yml
│   ├── scheduler.yml
│   └── autogen_config.yml
├── data_access/
│   ├── __init__.py
│   ├── database_connection.py
│   ├── query_executor.py
│   ├── schema_extractor.py
│   └── ddl_schemas/
│       └── *.sql
├── llm/
│   ├── __init__.py
│   ├── llm_interface.py
│   ├── sql_generator.py
│   ├── autogen_agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── database_schema_tool.py
│   │   ├── query_planner_tool.py
│   │   ├── data_profiler_tool.py
│   │   └── query_retriever_tool.py
│   ├── model/
│   │   ├── trained_model.pt
│   │   └── tokenizer.pkl
│   └── prompt.py
├── rag/
│   ├── __init__.py
│   ├── retriever.py
│   ├── setup_chromadb.py
│   └── vector_store/
│       ├── chromadb_client.py
│       └── question_sql_pairs.db
├── tableau_integration/
│   ├── __init__.py
│   ├── tableau_api.py
│   └── dashboard_parser.py
├── reporting/
│   ├── __init__.py
│   ├── insight_generator.py
│   └── report_formatter.py
├── scheduler/
│   ├── __init__.py
│   └── daily_tasks.py
├── ui/
│   ├── __init__.py
│   ├── app.py
│   ├── templates/
│   │   └── *.html
│   └── static/
│       ├── css/
│       └── js/
├── tests/
│   ├── __init__.py
│   ├── test_data_access.py
│   ├── test_llm.py
│   ├── test_rag.py
│   ├── test_tableau_integration.py
│   ├── test_reporting.py
│   ├── test_scheduler.py
│   └── test_autogen_agent.py
├── docs/
│   ├── requirements.txt
│   ├── architecture.md
│   ├── api_documentation.md
│   └── autogen_usage.md
└── scripts/
    ├── setup_env.sh
    └── deploy.sh
```

## Key Components

### Configuration
- **config/**: Contains configuration files for database, LLM, Tableau API, scheduler, and Autogen settings.

### Data Access
- **data_access/**: Manages database connections and schema extraction.
  - `database_connection.py`: Connects to IBM DB2 database.
  - `schema_extractor.py`: Extracts and stores database schemas.

### LLM
- **llm/**: Contains logic for the LLM agent and tools.
  - `autogen_agent.py`: Sets up the LLM agent using Autogen.
  - `tools/`: Includes tools like database schema, query planner, data profiler, and query retriever.
  - `prompt.py`: Stores prompts for the LLM.

### RAG (Retrieval-Augmented Generation)
- **rag/**: Manages the retrieval of query-SQL pairs.
  - `setup_chromadb.py`: Initializes ChromaDB from JSON files.
  - `vector_store/`: Contains ChromaDB client for managing vector data.

### Tableau Integration
- **tableau_integration/**: Interfaces with Tableau to fetch and parse dashboard data.

### Reporting
- **reporting/**: Generates insights and formats reports.

### Scheduler
- **scheduler/**: Handles scheduled tasks.

### UI
- **ui/**: Provides a Streamlit-based user interface for interaction.