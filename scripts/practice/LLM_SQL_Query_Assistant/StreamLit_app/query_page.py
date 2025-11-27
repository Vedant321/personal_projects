import streamlit as st
import pandas as pd
from db.postgres import PostgresDB
from gpt.sql_generator import SQLGenerator


st.set_page_config(page_title="Movie Records App", layout="wide")

def main_page():
    st.title("Movie Records Query App")

    db = PostgresDB()
    sql_gen = SQLGenerator()

    user_input = st.text_input("Enter your query in plain English:")

    if st.button("Generate SQL"):
        if user_input:
            try:
                sql_query = sql_gen.generate(user_input)
                st.code(sql_query, language='sql')
            except Exception as e:
                st.error(f"Error generating SQL: {e}")
        else:
            st.warning("Please enter a query.")

    if st.button("Execute SQL"):
        if user_input:
            try:
                sql_query = sql_gen.generate(user_input)
                
                if sql_query.lower().startswith("error"):
                    st.error(sql_query)
                else:
                    result = db.execute_query(sql_query)
                    if isinstance(result, pd.DataFrame):
                        st.dataframe(result)
                    else:
                        st.error(result)
            except Exception as e:
                st.error(f"Error executing SQL: {e}")
        else:
            st.warning("Please enter a query.")
