import streamlit as st

if __name__ == "__main__":
    st.title("Simple Chatbot")
    user_input = st.text_input("You:")
    if user_input:
        st.write(f"Bot: You said '{user_input}'!")
