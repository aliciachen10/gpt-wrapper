import streamlit as st 
import os
from page_nav import nav_page, next_page, prev_page, get_page

st.write("""
Now that you know these principles, let's practice motivating a 30-year-old depressed patient using the elicit-provide-elicit framework. If you like, you can go back to the previous screens and copy-paste information or take notes on a notepad file, and refer to that during your conversation. You will roleplay the role of peer counselor trained in MI, and you'll be talking to a 30-year old patient. Begin by using the elicit-provide-elicit framework, asking the client what ideas she has for how to feel better when she feels depressed. Then, continue to use the framework as you talk to her.

You can press "Switch to feedback mode" when you're finished wrapping up the conversation and want feedback on how it went.
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