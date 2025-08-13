import streamlit as st
import requests

st.title("LinkedIn AI Agent")

topic = st.text_input("Enter a topic")
if st.button("Generate Post"):
    resp = requests.post("http://localhost:8000/api/v1/generate/", params={"topic": topic})
    st.write(resp.json())
