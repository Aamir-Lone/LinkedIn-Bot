import streamlit as st
import datetime

def render_calendar():
    st.date_input("Select post date", datetime.date.today())
