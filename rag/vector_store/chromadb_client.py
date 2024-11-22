from chromadb import ChromaDB


class ChromaDBClient:
    def __init__(self, db_path):
        self.db = ChromaDB(db_path)
        self.db.initialize()

    def store_query_pair(self, query, sql):
        """Stores a query and its corresponding SQL in the vector store."""
        self.db.add_document({'query': query, 'sql': sql})

    def find_similar_queries(self, input_query, top_k=5):
        """Finds the most similar query-SQL pairs based on the input query."""
        results = self.db.query({'query': input_query}, top_k=top_k)
        return results
