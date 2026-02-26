import streamlit as st

st.markdown(
    """
    <style>
        html, body {
            background-color: white;
        }
        * {
            color: red !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to Northeastern University")

st.image("https://github.com/niletingham-web/IFCS_M12_Stretch_Streamlit/blob/main/NU_Logo.png?raw=true")

user_input = st.text_input("Your name")

course_input = st.text_input("What course are you studying?")

if user_input:
    st.write(f"Hello, {user_input.title()}, good luck studying {course_input.title()}!")