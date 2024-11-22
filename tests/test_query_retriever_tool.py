import unittest
from llm.tools.query_retriever_tool import QueryRetrieverTool


class TestQueryRetrieverTool(unittest.TestCase):
    def setUp(self):
        self.retriever = QueryRetrieverTool(db_path='path_to_chromadb')

    def test_retrieve_similar_queries(self):
        input_query = "SELECT * FROM customers WHERE age > 30"
        results = self.retriever.retrieve_similar_queries(input_query)
        self.assertIsInstance(results, list)

    def test_retrieve_similar_queries_no_results(self):
        input_query = "SELECT * FROM non_existent_table"
        results = self.retriever.retrieve_similar_queries(input_query)
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()
