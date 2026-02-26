import streamlit as st

st.title("Welcome to Northeastern University")

user_input = st.text_input("Your name")

if user_input:
    st.write(f"Hello, {user_input.title()}")