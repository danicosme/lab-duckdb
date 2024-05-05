from prettyconf import config
import duckdb
import os

def create_connection():
    return duckdb.connect(f"md:?motherduck_token={config('token')}")

def abspath(path):
    return os.path.abspath(path)

def csv_names(abs_path):
    return os.listdir(abs_path)

def execute_query(conn, query):
    return conn.sql(query)

def read_sql_file(path, **kwargs):
    with open(path) as f:
        file = f.read()
        return file.format(**kwargs)
