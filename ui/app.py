import streamlit as st
from llm.autogen_agent import initialize_agent
from llm.llm_interface import LLMInterface

# Initialize the agent and LLM interface
agent = initialize_agent()
llm_interface = LLMInterface(config_path='config/llm_config.yml')

st.title('GenAI Insurance Tool Chatbot')

st.write("""
Welcome to the GenAI Insurance Tool Chatbot! Enter your natural language query below, and our agent will process it to extract the SQL data table.
""")

# User input for natural language query
user_query = st.text_input("Enter your query:")

# Process the query and display results
if user_query:
    # Use the agent to process the input query
    sql_query = agent.process_query(user_query)
    st.write(f"Generated SQL Query: {sql_query}")

    # Execute the SQL query using the LLM interface
    result = llm_interface.execute_query(sql_query)
    if 'error' in result:
        st.error(f"Error: {result['error']}")
    else:
        st.write("Resulting Data Table:")
        st.dataframe(result)
