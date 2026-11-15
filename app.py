
import streamlit as st
from chatbot import get_answer

# Page configuration
st.set_page_config(
    page_title="Smart FAQ Chatbot",
    page_icon="🎓",
    layout="centered"
)

# Application heading
st.title("Smart FAQ Chatbot")
st.write("Ask questions about your college syllabus.")

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Question input
question = st.chat_input("Type your syllabus question here...")

if question:
    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            try:
                answer = get_answer(question)
            except Exception as error:
                answer = f"Something went wrong: {error}"

            st.write(answer)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
