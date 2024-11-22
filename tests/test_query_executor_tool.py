import unittest
from llm.tools.query_executor_tool import QueryExecutorTool


class TestQueryExecutorTool(unittest.TestCase):
    def setUp(self):
        self.executor = QueryExecutorTool()

    def test_execute_query(self):
        sql_query = "SELECT * FROM your_table LIMIT 1"
        result = self.executor.execute_query(sql_query)
        self.assertIsInstance(result, list)

    def test_execute_query_with_error(self):
        sql_query = "SELECT * FROM non_existent_table"
        result = self.executor.execute_query(sql_query)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
