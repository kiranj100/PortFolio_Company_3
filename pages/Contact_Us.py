import streamlit as st
from send_email import send_email
import pandas


df = pandas.read_csv("topics.csv")

st.set_page_config(layout="wide")

st.header("Contact US")

with st.form(key="email form"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox(
        'What topic do you want to discuss?',
         df['topic'])
    raw_message = st.text_area("Text")
    message = f"""\
Subject:New Email From {user_email} 

From: {user_email}
Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("your mail was send successfully")