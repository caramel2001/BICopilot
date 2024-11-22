from vector_store.chromadb_client import ChromaDBClient


class QueryRetrieverTool:
    def __init__(self, db_path):
        self.chroma_client = ChromaDBClient(db_path)

    def retrieve_similar_queries(self, input_query, top_k=5):
        """Retrieves the most similar query-SQL pairs based on the input query."""
        similar_pairs = self.chroma_client.find_similar_queries(input_query, top_k)
        return similar_pairs
