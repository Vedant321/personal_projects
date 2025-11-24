import psycopg2
import pandas as pd
from config import DB_CONFIG

class PostgresDB:
    def __init__(self, config=DB_CONFIG):
        self.config = config

    def get_connection(self):
        """Return a new DB connection"""
        return psycopg2.connect(**self.config)

    def execute_query(self, query):
        """
        Execute SQL query and return a pandas DataFrame
        """
        try:
            conn = self.get_connection()
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            return f"Error: {e}"
