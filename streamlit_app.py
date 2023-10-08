import streamlit as st
from langchain.llms import OpenAI

st.title('Train MI support skills')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Dummy text for demonstration purposes
text_blocks = [
    """
Offering MI-consistent information and advice consists of giving information in a way that supports the person’s autonomy and exploration of what, how, and when they might choose to make a change. We avoid direct persuasion or confrontation about what the person should do by infusing information and advice with collaboration and autonomy support. For example:				
* Prior to giving information or advice, we work to understand what the person already knows about their options or the topic and any specific ideas they are already interested in.
 						
* We tailor our advice or information to the person’s knowledge, situation, and preferences.
 						
* To avoid inadvertent persuasion, we frame information and advice in the form of a range of options that have helped others in similar situations.
 						
* When we do make specific recommendations for the person, we emphasize the person’s autonomy to choose for themselves.
 						
* After offering information or advice, we invite the person to explore how the information or advice may or may not work for them.
    """,
    """
*Elicit-provide-elicit* (sometimes known as ask-offer-ask or chunk-check-chunk) combines seeking collaboration and emphasizing autonomy:
 							
*Elicit* : Ask about the person’s own ideas and knowledge about the subject. For example:	

    * “What have you heard about the ways in which people get support to stop using substances?”				
    * “What ideas do you have for transportation?”			
    * “What health services would you like to learn more about?”
*Provide* : If it sounds like some advice or information would still be helpful, provide or offer this advice or information with permission (seeking collaboration). To preserve the collaboration and increase the likelihood that they will give these options some consideration, it’s important to give the person more than one option (and acknowledge the person’s freedom to disagree or ignore the information or advice). For example:	

	• “May I make a suggestion?”
 	• “Would you be interested in knowing about some resources?”
	• “I don’t know if this would interest you, but some people find...”
 							
*Elicit* : Ask for their response to the suggestion or information you have provided (seeking collaboration:	

    • “What do you think of these options for your situation?”
	• “You’re the expert here, how might these ideas work for you?” 
    • “Are you interested in trying any of these suggestions?” 	
    """,
    """
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
    """,
    """
## Avoiding Discord During Information Exchange

When offering information or feedback, we want to avoid triggering discord. We can change our approach to strengthen empathy and acceptance if discord emerges. For example: “It sounds like this doesn’t seem relevant to you. What do you feel is most important for us to talk about?” A few strategies for reducing the likelihood of discord when offering information include:				
    * Asking about what the person already knows and tailoring the information to what the person knows and is interested in changing (i.e., their strengths, goals, and needs).
 						
    * Offering information after the person asks for it.
 						
    * Asking permission to offer information.
 						
    * Supporting collaboration and autonomy (e.g., “You are the only person who can decide what makes the most sense for you in this situation.” “I’m interested in your thoughts about how this information applies to your situation.”). 

    """,
    """
Now that you know these principles, let's practice motivating a 30-year-old depressed patient using the elicit-provide-elicit framework. If you like, you can go back to the previous screens and copy-paste information or take notes on a notepad file, and refer to that during your conversation. You will roleplay the role of peer counselor trained in MI, and you'll be talking to a 30-year old patient. Begin by using the elicit-provide-elicit framework, asking the client what ideas she has for how to feel better when she feels depressed. Then, continue to use the framework as you talk to her.

You can press "Switch to feedback mode" when you're finished wrapping up the conversation and want feedback on how it went.
"""
]

# Set up state for current block index and whether the user has finished reading
if 'current_block' not in st.session_state:
    st.session_state['current_block'] = 0
if 'finished_reading' not in st.session_state:
    st.session_state['finished_reading'] = False

# If the user hasn't finished reading the blocks, show the blocks
if not st.session_state['finished_reading']:
    st.write(text_blocks[st.session_state['current_block']])
    
    if st.session_state['current_block'] > 0:
        if st.button("Previous"):
            st.session_state['current_block'] -= 1

    if st.session_state['current_block'] < len(text_blocks) - 1:
        if st.button("Next"):
            st.session_state['current_block'] += 1
    else:
        if st.button("Finish"):
            st.session_state['finished_reading'] = True

# existing GPT interaction code 
else:
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
            context_prompt = "you are a client working with me, your peer counselor. as a peer counselor, i am trained in motivational interviewing to help you work through a core dilemma. in your case, it would be getting help for your depression. let's roleplay, with me in the role of counselor and you in the role of depressed 30 year old woman who is ambivalent about doing anything about her depression. specifically, we are going to work through the elicit-provide-elicit framework for providing advice. i'll start"
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
                    # Button to switch to feedback mode placed outside of form context
            
            switch_to_feedback = st.button("Switch to Feedback Mode")
            if switch_to_feedback:
                st.session_state['feedback_mode'] = True
                    
        else:
            # Now in feedback mode
            master_trainer_prompt = ("you are a helpful expert MI trainer. looking at the content of this conversation, can you provide feedback for specifically: 1. how I did with the elicit-provide-elicit framework, 2. anything I could improve in general, specifically with regard to adherence to the MI core principles and framework in general, and 3. what I did well ")
            full_feedback_prompt = f"{master_trainer_prompt}\n\nConversation:\n"
            
            # Construct the full feedback prompt with conversation history
            for exchange in conversation_history:
                role_icon = "👤" if exchange['role'] == 'user' else "🤖"
                full_feedback_prompt += f"{role_icon}: {exchange['message']}\n"
            
            # Get model's feedback
            feedback = llm(full_feedback_prompt)
            st.write(f"📋 Feedback:\n{feedback}")
            
            # Button to restart roleplaying (resetting everything)
            reset_button = st.button("Restart Roleplaying")
            if reset_button:
                st.session_state.pop('feedback_mode', None)
                st.session_state.pop('conversation', None)
