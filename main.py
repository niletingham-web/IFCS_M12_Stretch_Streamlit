import streamlit as st

st.title("Welcome to Northeastern University")

user_input = st.text_input("Your name")

course_input = st.text_input("What course are you studying?")

if user_input:
    st.write(f"Hello, {user_input.title()}, good luck studying {course_input.title()}")