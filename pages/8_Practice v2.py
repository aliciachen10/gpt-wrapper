import streamlit as st
import openai
import os 
from openai import OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

my_assistant = client.beta.assistants.create(
    instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    name="Math Tutor",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = "user",
    content = "Help me devide 10 by pi"
)

run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id,
    instruction = "Please helpt the user."
)

import time
time.sleep(10)
print(run)
run_status = client.beat.threads.run.retrieve(
    thread_id = thread.id,
    run_id = run.id
)
# # Initialize OpenAI API
# openai.api_key = st.secrets["OPENAI_API_KEY"]

# # Create Assistants
# client_assistant = openai.Assistant.create(
#     name="peer counseling client",
#     instructions="You are a client in peer counseling, and you present with depression. Respond to me as if I am your peer counselor.",
#     model="gpt-4"
# )

# feedback_assistant = openai.Assistant.create(
#     name="feedback assistant",
#     instructions="You are an expert motivational interviewing trainer and clinical psychologist. Please provide feedback on the following conversation as if you are this peer counselor's supervisor on 1) what the peer counselor did well, citing specific motivational interviewing techniques that were well employed, and 2) what they could have improved upon.",
#     model="gpt-4"
# )

# # Initialize session state for conversation history
# if 'conversation' not in st.session_state:
#     st.session_state.conversation = []

# # Chat interface
# st.title("Peer Counseling Roleplay")
# user_input = st.text_input("Your message as a peer counselor:", key='user_input')

# if st.button("Send"):
#     st.session_state.conversation.append({"role": "Peer Counselor", "message": user_input})
#     response = client_assistant.chat(user_input)
#     st.session_state.conversation.append({"role": "Client", "message": response})
#     st.text_area("Conversation", "\n".join(f"{x['role']}: {x['message']}" for x in st.session_state.conversation), height=300, disabled=True)

# # Feedback mode
# if st.button("Feedback"):
#     st.session_state.feedback_mode = True

# if st.session_state.get('feedback_mode', False):
#     st.title("Feedback on Conversation")
#     conversation_text = "\n".join(f"{x['role']}: {x['message']}" for x in st.session_state.conversation)
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.text_area("Conversation", conversation_text, height=300, disabled=True)

#     with col2:
#         feedback = feedback_assistant.chat(conversation_text)
#         st.text_area("Feedback", feedback, height=300, disabled=True)