import streamlit as st
from app.pages import page1

def main():
    st.title("Streamlit Project")
    page1.display_page()

if __name__ == "_main_":
    main()
