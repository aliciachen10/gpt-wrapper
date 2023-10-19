import streamlit as st 
import os
from page_nav import nav_page, next_page, prev_page, get_page

st.write( """
## Avoiding Discord During Information Exchange

When offering information or feedback, we want to avoid triggering discord. We can change our approach to strengthen empathy and acceptance if discord emerges. For example: “It sounds like this doesn’t seem relevant to you. What do you feel is most important for us to talk about?” A few strategies for reducing the likelihood of discord when offering information include:				
    * Asking about what the person already knows and tailoring the information to what the person knows and is interested in changing (i.e., their strengths, goals, and needs).
 						
    * Offering information after the person asks for it.
 						
    * Asking permission to offer information.
 						
    * Supporting collaboration and autonomy (e.g., “You are the only person who can decide what makes the most sense for you in this situation.” “I’m interested in your thoughts about how this information applies to your situation.”). 

         
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