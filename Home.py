import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.title("The Best Company")
summery = st.write ("""
Sure! "InnovateTech Solutions is a cutting-edge technology firm specializing in 
artificial intelligence and software development. Our team of experts creates innovative 
solutions to empower businesses with transformative digital capabilities. 
From advanced AI applications to custom software development, we deliver tailored solutions 
to meet the evolving needs of our clients. Committed to excellence, we strive to drive 
technological advancements and elevate businesses to new heights.
""")


st.subheader("Our Team")


col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

#add content of first column
with col1:
    # Iterate only first 4 row
    for index, row in df[:4].iterrows():
        #add members first and last name
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        #add members role in company
        st.write(row["role"])
        #add memebers photo's
        st.image("images/" + row["image"])
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])





