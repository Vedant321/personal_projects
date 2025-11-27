import streamlit as st
from auth.users import validate_user

def login_page():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.success("Welcome back!")
        return True  # Already logged in

    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_user(username, password):
            st.session_state.logged_in = True
            st.success(f"Welcome, {username}!")
            # No need to call experimental_rerun()
        else:
            st.error("Invalid username or password")

    return st.session_state.logged_in
