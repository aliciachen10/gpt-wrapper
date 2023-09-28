import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Chat with OpenAI')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Ensure the OpenAI API key is set
if not openai_api_key or not openai_api_key.startswith('sk-'):
    st.warning('Please enter a valid OpenAI API key!', icon='⚠')
else:
    # Initialize the OpenAI model
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    # Get stored conversation or start a new one
    conversation_history = st.session_state.get('conversation', [])

    # Display the conversation history
    for exchange in conversation_history:
        if exchange['role'] == 'user':
            st.write(f"👤: {exchange['message']}")
        else:
            st.write(f"🤖: {exchange['message']}")

    # Input area for user's message
    user_input = st.text_input('Your Message:')

    if st.button('Send'):
        # Add user's message to the conversation
        conversation_history.append({'role': 'user', 'message': user_input})

        # Get model's response
        model_response = llm(user_input)
        conversation_history.append({'role': 'model', 'message': model_response})

        # Save conversation to the session state
        st.session_state['conversation'] = conversation_history

        # Refresh the page to display the updated conversation
        st.experimental_rerun()
