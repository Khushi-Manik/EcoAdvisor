import streamlit as st
from app.pages import page1

def main():
    st.title("Streamlit Project")
    page1.display_page()

if _name_ == "_main_":
    main()
