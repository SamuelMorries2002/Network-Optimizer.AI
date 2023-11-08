import streamlit as st
from traffic_generator import run_traffic

st.title("My Streamlit Website") 

st.header("Hello, World!")

name = st.text_input("Enter your name:")

st.write(f"Hello, {name}!")

st.write("This is a simple website created with Streamlit.")

#if st.button("Generate Traffic"):
    #run_traffic() 

st.write("Traffic generated!")
