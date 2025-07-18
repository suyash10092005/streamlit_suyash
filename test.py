import streamlit as st

st.title("Welcome!")

st.write("Hi, I am Suyash, Nice to meet you.")
st.write("What's your name?")

user_name = st.text_input("Enter your name:")

if st.button("Submit"):
    if user_name:
        st.success(f"Hi {user_name}. Nice to meet you!")
    else:
        st.warning("Please enter your name before submitting.")
