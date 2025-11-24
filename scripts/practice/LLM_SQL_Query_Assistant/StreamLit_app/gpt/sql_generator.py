import openai
from config import DB_CONFIG, OPENAI_API_KEY


class SQLGenerator:
    def __init__(self, api_key=OPENAI_API_KEY, model="gpt-4"):
        openai.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> str:
        """
        Generate SQL query from plain text prompt
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a PostgreSQL assistant."},
                    {"role": "user", "content": f"Generate a PostgreSQL query for: {prompt}"}
                ],
                max_tokens=200
            )
            sql_query = response['choices'][0]['message']['content'].strip()
            return sql_query
        except Exception as e:
            return f"Error generating SQL: {e}"
