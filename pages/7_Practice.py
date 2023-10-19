import streamlit as st 
from langchain.llms import OpenAI
import psycopg2
import os
import urllib.parse as up
from dotenv import load_dotenv

load_dotenv()

up.uses_netloc.append("postgres")
# url = up.urlparse(os.environ["DATABASE_URL"])

# st.write("DB username:", st.secrets["db_username"])
url = up.urlparse(st.secrets["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM conversations LIMIT 5")  # Replace with your table name
records = cursor.fetchall()

st.title('Train MI support skills')

openai_api_key = st.secrets["OPENAI_API_KEY"]
# openai_api_key = st.sidebar.text_input('OpenAI API Key')

st.write("""
Now that you know these principles, let's practice motivating a 30-year-old depressed patient using the elicit-provide-elicit framework. If you like, you can go back to the previous screens and copy-paste information or take notes on a notepad file, and refer to that during your conversation. You will roleplay the role of peer counselor trained in MI, and you'll be talking to a 30-year old patient. Begin by using the elicit-provide-elicit framework, asking the client what ideas she has for how to feel better when she feels depressed. Then, continue to use the framework as you talk to her.

You can press "Switch to feedback mode" when you're finished wrapping up the conversation and want feedback on how it went.
""")
# Ensure the OpenAI API key is set
if not openai_api_key or not openai_api_key.startswith('sk-'):
    st.warning('Please enter a valid OpenAI API key!', icon='⚠')
else:
    # Initialize the OpenAI model
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    # Get stored conversation or start a new one
    conversation_history = st.session_state.get('conversation', [])
    
    # Check if in feedback mode or not
    feedback_mode = st.session_state.get('feedback_mode', False)

    if not feedback_mode:
        # Contextual prompt for roleplaying
        context_prompt = "you (GPT) are a depressed client working with me, your peer counselor. as a peer counselor, i (the user) am trained in motivational interviewing to help you work through a core dilemma. in your case, it would be getting help for your depression. let's roleplay, with me (the user) in the role of counselor and you (GPT) in the role of depressed 30 year old woman who is ambivalent about doing anything about her depression. please ONLY play the role of the depressed 30-year old client, and do not say anyl lines that the counselor would say. do not use emojis or punctuation to start your responses -- start your responses as if you are merely playing the role of that patient. specifically, we are going to work through the elicit-provide-elicit framework for providing advice. i'll start"
    # Generate full conversation with context
        conversation_text = context_prompt

        # Display the conversation history
        for exchange in conversation_history:
            if exchange['role'] == 'user':
                st.write(f"👤: {exchange['message']}")
            else:
                st.write(f"🤖: {exchange['message']}")

        for exchange in conversation_history:
            role_icon = "👤" if exchange['role'] == 'user' else "🤖"
            conversation_text += f"\n{role_icon}: {exchange['message']}"
            ### INSERT HERE###
            # Define the SQL query with placeholders for the parameters
            sql = "INSERT INTO conversations (role_column, message_column) VALUES (%s, %s)"
            # Define the values to be inserted
            values = (exchange['role'], exchange['message'])

            cursor.execute(sql, values)
            # Commit the transaction to save the changes to the database
            conn.commit()
        with st.form(key='chatbox'):
            user_input = st.text_area('Your Message:', max_chars=500, height=100, key='user_input')
            send_button = st.form_submit_button('Send')

            if send_button and user_input:
                # Add user's message to the conversation
                conversation_history.append({'role': 'user', 'message': user_input.strip()})

                # Combine context with user's message
                # full_prompt = f"{context_prompt}\nUser: {user_input}"
                full_prompt = f"{conversation_text}\n👤: {user_input}"

                # Get model's response
                # model_response = llm(user_input) # original input
                model_response = llm(full_prompt)
                conversation_history.append({'role': 'model', 'message': model_response})

                # Save conversation to the session state
                st.session_state['conversation'] = conversation_history
                # print("CONVERSATION HISTORY", st.session_state['conversation'])

                # Refresh the page to display the updated conversation
                st.experimental_rerun()
                # Button to switch to feedback mode placed outside of form context
        
        switch_to_feedback = st.button("Switch to Feedback Mode")
        # if switch_to_feedback:
        #     st.session_state['feedback_mode'] = True

        # Button to switch to feedback mode (outside of the above if condition)
        if switch_to_feedback and not st.session_state['feedback_mode']:
            st.session_state['feedback_mode'] = True
    else:
        # Now in feedback mode
        master_trainer_prompt = ("you are a helpful expert MI trainer. looking at the content of this conversation, can you provide feedback for specifically: 1. how I did with the elicit-provide-elicit framework, 2. anything I could improve in general, specifically with regard to adherence to the MI core principles and framework in general, and 3. what I did well ")
        full_feedback_prompt = f"{master_trainer_prompt}\n\nConversation:\n"
        
        # Construct the full feedback prompt with conversation history
        for exchange in conversation_history:
            role_icon = "👤" if exchange['role'] == 'user' else "🤖"
            full_feedback_prompt += f"{role_icon}: {exchange['message']}\n"

        col1, col2 = st.columns(2)
        
        # render in the original conversation
        with col1: 
            st.write(f"original conversation:")
            for exchange in conversation_history:
                role_icon = "👤" if exchange['role'] == 'user' else "🤖"
                st.write(f"\n{role_icon}: {exchange['message']}")

        # Get model's feedback
        feedback = llm(full_feedback_prompt)

        with col2: 
            st.write(f"📋 Feedback:\n{feedback}")
            
            # Button to restart roleplaying (resetting everything)
            reset_button = st.button("Restart Roleplaying")
            if reset_button:
                st.session_state.pop('feedback_mode', None)
                st.session_state.pop('conversation', None)
