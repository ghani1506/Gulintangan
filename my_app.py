import streamlit as st

st.title("My Interactive App")
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")