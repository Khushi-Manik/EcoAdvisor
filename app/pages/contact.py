import streamlit as st
import re

# Set up the page configuration
st.set_page_config(page_title="Contact Us", layout="wide")

# Define the color scheme
primary_green = "#1b4d3e"
darker_green = "#1c352d"
accent_green = "#014421"
background_color = "#FFFFFF"
header_background_color = darker_green
header_text_color = "#FFFFFF"
section_background_color = primary_green
section_text_color = "#FFFFFF"
input_text_color = "#000000"  # Black color for input text
required_star_color = "#f44336"  # Red color for required star

# Apply custom styles
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color};
    }}
    .stTitle {{
        color: {header_text_color};
        background-color: {header_background_color};
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        font-size: 2.5em;
        margin: 0;
        border-bottom: 4px solid {accent_green};
    }}
    .header {{
        display: flex;
        align-items: center;
        padding: 20px;
    }}
    .header img {{
        margin-right: 15px;
        width: 120px; /* Adjust width for the logo here */
        height: auto;
    }}
    .section {{
        border: 2px solid {accent_green};
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
        background-color: {section_background_color};
        color: {section_text_color};
        text-align: center; /* Center-align the content */
    }}
    .section h2 {{
        color: {header_text_color};
    }}
    .stButton button {{
        margin-top: 20px;
        padding: 10px 20px;
        background-color: {accent_green};
        color: {header_text_color};
        border: none;
        border-radius: 8px;
        cursor: pointer;
        width: 100%;
    }}
    .stButton button:hover {{
        background-color: {darker_green};
    }}
    .stTextInput input {{
        background-color: {background_color};
        color: {input_text_color};
        border: 2px solid {accent_green};
        border-radius: 4px;
        padding: 10px;
        width: 100%;
    }}
    .stTextArea textarea {{
        background-color: {background_color};
        color: {input_text_color};
        border: 2px solid {accent_green};
        border-radius: 4px;
        padding: 10px;
        width: 100%;
    }}
    .required {{
        color: {input_text_color}; /* Black color for the label text */
    }}
    .required-star {{
        color: {required_star_color}; /* Red color for the star */
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header with title
st.markdown('<div class="stTitle">Contact Us</div>', unsafe_allow_html=True)

# Contact form
st.markdown('<div class="section"><h2>Get in Touch</h2></div>', unsafe_allow_html=True)

with st.form(key='contact_form'):
    st.markdown('<div class="required"><span class="required-star">*</span> Name:</div>', unsafe_allow_html=True)
    name = st.text_input("", key="name")
    
    st.markdown('<div class="required"><span class="required-star">*</span> Email:</div>', unsafe_allow_html=True)
    email = st.text_input("", key="email")
    
    st.markdown('<div class="required"><span class="required-star">*</span> Subject:</div>', unsafe_allow_html=True)
    subject = st.text_input("", key="subject")
    
    st.markdown('<div class="required"><span class="required-star">*</span> Message:</div>', unsafe_allow_html=True)
    message = st.text_area("", key="message")

    submit_button = st.form_submit_button("Submit")

if submit_button:
    # Form validation
    if not name or not email or not subject or not message:
        st.markdown(
            '<div class="section"><h2 style="color: #f44336;">Please fill out all required fields before submitting.</h2></div>',
            unsafe_allow_html=True,
        )
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.markdown(
            '<div class="section"><h2 style="color: #f44336;">Please enter a valid email address.</h2></div>',
            unsafe_allow_html=True,
        )
    else:
        # In a real-world scenario, you would handle form submission here
        st.markdown(
            f'<div class="section"><h2>Thank you, {name}!</h2><p>Your message has been received. We will get back to you soon.</p></div>',
            unsafe_allow_html=True,
        )
