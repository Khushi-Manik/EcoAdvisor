import streamlit as st

st.title("Guidelines Document")

# URL to the document
url = "https://docs.google.com/document/d/1HImWJDr76ngXtWfQYAOwLUBQB1NacHg9j2P5casaV-M/edit"

# Create a clickable link
st.markdown(f"[Click here to open the guidelines]({url})")