import streamlit as st
import os
from page_nav import nav_page, next_page, prev_page, get_page


st.title("Train MI support skills")

st.write("""
*Elicit-provide-elicit* (sometimes known as ask-offer-ask or chunk-check-chunk) combines seeking collaboration and emphasizing autonomy:
 							
*Elicit* : Ask about the person’s own ideas and knowledge about the subject. For example:	

    * “What have you heard about the ways in which people get support to stop using substances?”				
    * “What ideas do you have for transportation?”			
    * “What health services would you like to learn more about?”
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
