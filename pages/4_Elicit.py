import streamlit as st 
import os
from page_nav import nav_page, next_page, prev_page, get_page

st.write("""
*Elicit* : Ask for their response to the suggestion or information you have provided (seeking collaboration:	

    • “What do you think of these options for your situation?”
	• “You’re the expert here, how might these ideas work for you?” 
    • “Are you interested in trying any of these suggestions?” 	
    """)

button_column_1, button_column_2 = st.columns(2) 

with button_column_1: 
    if st.button("Previous"):
        # nav_page("module_2")
        get_page(os.path.basename(__file__), "previous")

with button_column_2: 
    if st.button("Next"):
        # nav_page("module_2")
        get_page(os.path.basename(__file__), "next")