import streamlit as st
from db.postgres import PostgresDB
from gpt.sql_generator import SQLGenerator
import pandas as pd
st.set_page_config(page_title="Patient Records App", layout="wide")
st.title("Patient Records Query App")

# --- Instantiate classes ---
db = PostgresDB()
sql_gen = SQLGenerator()

# --- Streamlit input ---
user_input = st.text_input("Enter your query in plain English:")

if st.button("Generate SQL"):
    if user_input:
        sql_query = sql_gen.generate(user_input)
        st.code(sql_query, language='sql')
    else:
        st.warning("Please enter a query.")

if st.button("Execute SQL"):
    if user_input:
        sql_query = sql_gen.generate(user_input)
        result = db.execute_query(sql_query)
        if isinstance(result, pd.DataFrame):
            st.dataframe(result)
        else:
            st.error(result)
    else:
        st.warning("Please enter a query.")
