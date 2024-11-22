import ibm_db


def get_connection():
    dsn = (
        "DRIVER={{IBM DB2 ODBC DRIVER}};"
        "DATABASE=your_database_name;"
        "HOSTNAME=your_host_name;"
        "PORT=your_port_number;"
        "PROTOCOL=TCPIP;"
        "UID=your_user_id;"
        "PWD=your_password;"
    )
    connection = ibm_db.connect(dsn, "", "")
    return connection
