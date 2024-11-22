import json
from vector_store.chromadb_client import ChromaDBClient


def setup_chromadb_from_json(json_file_path, db_path):
    """Creates a ChromaDB and adds all query-SQL pairs from a JSON file."""
    with open(json_file_path, 'r') as file:
        query_sql_pairs = json.load(file)

    chroma_client = ChromaDBClient(db_path)

    for pair in query_sql_pairs:
        query = pair.get('query')
        sql = pair.get('sql')
        if query and sql:
            chroma_client.store_query_pair(query, sql)

    return chroma_client
