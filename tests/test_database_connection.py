import unittest
from data_access.database_connection import get_connection


class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        connection = get_connection()
        self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main()
