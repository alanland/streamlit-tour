import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
date = st.date_input("Pick a date")
