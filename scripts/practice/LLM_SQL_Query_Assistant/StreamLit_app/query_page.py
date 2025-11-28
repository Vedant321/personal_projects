import streamlit as st
import pandas as pd
from db.postgres import PostgresDB
from gpt.sql_generator import SQLGenerator

def main_page():
    st.markdown("<h1>🍿 Movie Database Explorer</h1>", unsafe_allow_html=True)

    db = PostgresDB()
    sql_gen = SQLGenerator()

    # User Query Section
    st.markdown("<div class='netflix-card'>", unsafe_allow_html=True)
    user_input = st.text_input("Ask something about movies…")
    st.markdown("</div>", unsafe_allow_html=True)

    # Generate SQL
    if st.button("Generate SQL"):
        if user_input:
            sql_query = sql_gen.generate(user_input)
            st.markdown("<div class='netflix-card'>", unsafe_allow_html=True)
            st.subheader("🧠 Generated SQL")
            st.code(sql_query, language='sql')
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a query.")

    # Execute SQL
    if st.button("Run Query"):
        if user_input:
            sql_query = sql_gen.generate(user_input)
            result = db.execute_query(sql_query)
            st.markdown("<div class='netflix-card'>", unsafe_allow_html=True)
            st.subheader("📊 Results")
            if isinstance(result, pd.DataFrame):
                st.dataframe(result)
            else:
                st.error(result)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a query.")
