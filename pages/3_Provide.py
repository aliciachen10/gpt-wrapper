import streamlit as st
import os
from page_nav import nav_page, next_page, prev_page, get_page

st.write("""
*Provide* : If it sounds like some advice or information would still be helpful, provide or offer this advice or information with permission (seeking collaboration). To preserve the collaboration and increase the likelihood that they will give these options some consideration, it’s important to give the person more than one option (and acknowledge the person’s freedom to disagree or ignore the information or advice). For example:	

	• “May I make a suggestion?”
 	• “Would you be interested in knowing about some resources?”
	• “I don’t know if this would interest you, but some people find...”
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