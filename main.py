import streamlit as st

st.markdown(
    """
    <style>
        html, body, [class*="css"]  {
            color: red !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to Northeastern University")

user_input = st.text_input("Your name")

course_input = st.text_input("What course are you studying?")

if user_input:
    st.write(f"Hello, {user_input.title()}, good luck studying {course_input.title()}!")