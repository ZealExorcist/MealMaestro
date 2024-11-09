import requests
import streamlit as st
import os
import google.generativeai as genai


st.title("Recipe Finder")

with st.spinner():
    st.write("Enter the food item you want to search for:")
    input = st.text_input("Enter food item")
    prompt = st.session_state.prompt + "recipe for " + input
    if st.button("Search"):
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"recipe for {input}")
        st.markdown(response.text)

