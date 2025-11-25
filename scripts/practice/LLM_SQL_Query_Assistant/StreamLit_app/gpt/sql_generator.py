from openai import OpenAI
from config import OPENAI_API_KEY

class SQLGenerator:
    def __init__(self, api_key=OPENAI_API_KEY):
        self.client = OpenAI(api_key=api_key)

    def generate(self, user_query: str) -> str:
        """
        Generate SQL query from a natural language query.
        Returns only SQL code as a string.
        """
        table_schema = "movies(title TEXT, release_year INT, genre TEXT, rating FLOAT)"

        prompt = f""" You are a SQL assistant. The database has the following table schema:

                {table_schema}

                Generate a SQL query to answer this user request:
                "{user_query}"

                Return ONLY the SQL query, no explanations.
                """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a SQL assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )

            sql_query = response.choices[0].message.content.strip()

            if sql_query.lower().startswith("sql"):
                sql_query = sql_query[3:].strip()

            return sql_query

        except Exception as e:
            return f"Error generating SQL: {e}"
