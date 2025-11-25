# app.py
import streamlit as st
import pandas as pd
from db.postgres import PostgresDB
from gpt.sql_generator import SQLGenerator

# --- Streamlit page config ---
st.set_page_config(page_title="Movie Records App", layout="wide")
st.title("Movie Records Query App")

# --- Instantiate classes ---
db = PostgresDB()
sql_gen = SQLGenerator()

# --- Streamlit input ---
user_input = st.text_input("Enter your query in plain English:")

# --- Button: Generate SQL ---
if st.button("Generate SQL"):
    if user_input:
        try:
            sql_query = sql_gen.generate(user_input)
            st.code(sql_query, language='sql')
        except Exception as e:
            st.error(f"Error generating SQL: {e}")
    else:
        st.warning("Please enter a query.")

# --- Button: Execute SQL ---
if st.button("Execute SQL"):
    if user_input:
        try:
            sql_query = sql_gen.generate(user_input)
            # If GPT returned an error message, show it instead of executing
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
