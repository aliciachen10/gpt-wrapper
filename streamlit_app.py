import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Chat with Your Coach')

# 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
openai_api_key = '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' or st.sidebar.text_input('OpenAI API Key')

# print("API_KEY" + openai_api_key)

# Ensure the OpenAI API key is set
if not openai_api_key or not openai_api_key.startswith('sk-'):
    st.warning('Please enter a valid OpenAI API key!', icon='⚠')
else:
    # Initialize the OpenAI model
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    # Get stored conversation or start a new one
    conversation_history = st.session_state.get('conversation', [])

    # Contextual prompt
    context_prompt = "you are a client working with me, your peer counselor. as a peer counselor, i am trained in motivational interviewing to help you work through a core dilemma. in your case, it would be getting help for your depression. let's roleplay, with me in the role of counselor and you in the role of depressed 30 year old woman who is ambivalent about doing anything about her depression. specifically, we are going to work through the elicit-provide-elicit framework for providing advice. i'll start"
    # Generate full conversation with context
    conversation_text = context_prompt
    # Display the conversation history
    # original code here 
    for exchange in conversation_history:
        if exchange['role'] == 'user':
            st.write(f"👤: {exchange['message']}")
        else:
            st.write(f"🤖: {exchange['message']}")

    for exchange in conversation_history:
        role_icon = "👤" if exchange['role'] == 'user' else "🤖"
        # try to substitute instead of icon, using "user" and "patient"
        conversation_text += f"\n{role_icon}: {exchange['message']}"
    

    # Chatbox for back and forth interaction
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

        # Refresh the page to display the updated conversation
        st.experimental_rerun()
