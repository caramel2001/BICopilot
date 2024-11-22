class Prompts:
    @staticmethod
    def text_to_sql_prompt(query):
        return f"Translate the following natural language query into SQL: '{query}'"

    @staticmethod
    def dashboard_insight_prompt(dashboard_data):
        return f"Generate insights from the following Tableau dashboard data: {dashboard_data}"

    @staticmethod
    def query_similarity_prompt(input_query):
        return f"Find similar queries to: '{input_query}'"
