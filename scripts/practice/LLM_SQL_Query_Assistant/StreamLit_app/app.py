from auth.login import login_page
from query_page import main_page

# Show login page first
if login_page():
    main_page()

#streamlit run app.py --server.runOnSave true
# Sample queries:
#1. Give me list of all action movies.
#2. Give me list of all actors and their movies who's name starts with T