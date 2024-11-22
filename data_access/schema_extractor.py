from database_connection import get_connection
import ibm_db

def extract_schemas():
    connection = get_connection()
    sql = "SELECT TABNAME, TEXT FROM SYSCAT.VIEWS WHERE TYPE='T'"
    stmt = ibm_db.exec_immediate(connection, sql)
    result = ibm_db.fetch_assoc(stmt)
    while result:
        table_name = result['TABNAME']
        ddl = result['TEXT']
        with open(f'ddl_schemas/{table_name}.sql', 'w') as file:
            file.write(ddl)
        result = ibm_db.fetch_assoc(stmt)
