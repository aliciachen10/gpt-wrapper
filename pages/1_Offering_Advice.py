import streamlit as st 
import os
from page_nav import nav_page, next_page, prev_page, get_page

# Initialize session state
session_state = st.session_state
# if not hasattr(session_state, "current_page"):
#     session_state.current_page = "Module 1"

st.title('Train MI support skills')

st.write(""" 
Offering MI-consistent information and advice consists of giving information in a way that supports the person’s autonomy and exploration of what, how, and when they might choose to make a change. We avoid direct persuasion or confrontation about what the person should do by infusing information and advice with collaboration and autonomy support. For example:				
* Prior to giving information or advice, we work to understand what the person already knows about their options or the topic and any specific ideas they are already interested in.
 						
* We tailor our advice or information to the person’s knowledge, situation, and preferences.
 						
* To avoid inadvertent persuasion, we frame information and advice in the form of a range of options that have helped others in similar situations.
 						
* When we do make specific recommendations for the person, we emphasize the person’s autonomy to choose for themselves.
 						
* After offering information or advice, we invite the person to explore how the information or advice may or may not work for them.

""")

if st.button("Next"):
    # nav_page("module_2")
    get_page(os.path.basename(__file__), "next")

# next_button = st.button("Module 2")

# if next_button: 
#     session_state.current_page = "Module 2"