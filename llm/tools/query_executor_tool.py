from data_access.database_connection import get_connection
import ibm_db


class QueryExecutorTool:
    def execute_query(self, sql_query):
        """Executes the given SQL query on the IBM DB2 database and returns the results or an error message."""
        connection = get_connection()
        try:
            stmt = ibm_db.exec_immediate(connection, sql_query)
            result = []
            row = ibm_db.fetch_assoc(stmt)
            while row:
                result.append(row)
                row = ibm_db.fetch_assoc(stmt)
            return result
        except Exception as e:
            return {'error': str(e)}
