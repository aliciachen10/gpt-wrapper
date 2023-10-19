import streamlit as st 
import os
from page_nav import nav_page, next_page, prev_page, get_page

st.write("""
Elicit-provide-elicit could look like this:					

**Practitioner** [elicit]: “What do you know about the connection between what people do and how they feel?”				

**Person:** “Well, last time we talked we figured out that I feel better after I do little things, like take a shower.”		

**Practitioner** [elicit]: “Right—that’s exactly what I’m asking about. What else do you remember?”					

**Person:** “That when I didn’t do anything, I felt worse.”					

**Practitioner** [provide]: “Yes, you noticed a pattern where mornings before your shower and walk you felt worse, and then after your shower and walk you felt a bit better. We talked about possibly scheduling some more pleasant activities into your week to see how you feel then. What do you think about working on that together today?”		

**Person:** “Um...okay, but do I have to come up with the activities?”

**Practitioner [elicit]:** “Well, if you want, we can start with your ideas. And then if it’s helpful, I can offer some additional ideas that other people have found helpful [potentially provide]. But really, you are the expert on what will work best for you [emphasize autonomy]. What do you think? Should we try this out [seek collaboration]?”

MI-consistent information exchange helps to increase participation in sorting through information and ideas for interventions and activities. Emphasizing the person’s expertise about what will work for them helps them bring forward their ideas and avoid passive agreement with our ideas.

This may be particularly true when we are working with young people. Asking permission to explore topics and exchange information demonstrates respect for the person’s choices and capabilities. Following new information with interest in their thoughts about how it might fit for them supports autonomy and collaboration. This MI-consistent way of offering information helps us to partner with young people to develop options and solutions. It provides a safe and collaborative environment where they can explore their own thoughts and make decisions.
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