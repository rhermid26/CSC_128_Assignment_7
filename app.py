import streamlit as st
from agent import run_agent


st.title("Study Room Assistant")

st.caption("You are chatting with an automated assistant, not a person.")


# Store the conversation
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Get new user message
if prompt := st.chat_input("Ask about study rooms..."):

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Get assistant response
    with st.chat_message("assistant"):
        try:
            response = run_agent(st.session_state.messages.copy())

            st.write(response)

            # Save assistant response
            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })

        except Exception as error:
            st.error(f"Something went wrong: {error}")