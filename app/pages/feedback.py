import streamlit as st

# Define the color scheme
primary_green = "#1b4d3e"  # Darker shade of green
darker_green = "#1c352d"  # Dark green for header
accent_green = "#014421"  # Accent green for buttons
background_color = "#FFFFFF"  # White background for a clean look
header_background_color = darker_green
header_text_color = "#FFFFFF"
section_background_color = primary_green
section_text_color = "#FFFFFF"
input_text_color = "#000000"  # Black color for input text
label_text_color = primary_green  # Use primary green for label text

# Apply custom CSS styles
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color};
    }}
    .header {{
        background-color: {header_background_color};
        color: {header_text_color};
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
    }}
    .header h1 {{
        color: {header_text_color};  /* Set header title color to white */
    }}
    .section {{
        background-color: {section_background_color};
        color: {section_text_color};
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    .section h2 {{
        color: {section_text_color};  /* Set section title color to white */
    }}
    .submit-btn {{
        background-color: {accent_green};
        color: #FFFFFF;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }}
    .submit-btn:hover {{
        background-color: #007200;
    }}
    .stTextInput > div > label, .stTextArea > div > label {{
        color: {label_text_color} !important;
        font-weight: bold;
    }}
    .stTextInput > div > input {{
        background-color: {background_color};
        color: {input_text_color} !important;
        border: 2px solid {accent_green};
        border-radius: 4px;
        padding: 10px;
    }}
    .stTextArea > div > textarea {{
        background-color: {background_color};
        color: {input_text_color} !important;
        border: 2px solid {accent_green};
        border-radius: 4px;
        padding: 10px;
    }}
    .stSlider > div[data-baseweb="slider"] > div:first-child > div {{
        background-color: {primary_green} !important;
    }}
    .stSlider > div > div {{
        color: {label_text_color} !important;
    }}
    .stRadio > div > label > div[data-baseweb="radio"] {{
        background-color: {primary_green} !important;
    }}
    .stRadio > div > label {{
        color: {label_text_color} !important;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Set the title with a refined color scheme
    st.markdown('<div class="header"><h1>Feedback Form</h1></div>', unsafe_allow_html=True)

    # Create a form for feedback submission
    with st.form(key='feedback_form'):
        # Personal Information
        st.markdown('<div class="section"><h2>Personal Information</h2></div>', unsafe_allow_html=True)

        name = st.text_input('Name', key='name')
        email = st.text_input('Email', key='email')
        phone_number = st.text_input('Phone Number', key='phone_number')

        # User Experience
        st.markdown('<div class="section"><h2>User Experience</h2></div>', unsafe_allow_html=True)

        experience_rating = st.slider(
            'How would you rate your experience while browsing our website?',
            min_value=1, max_value=5, value=3, step=1
        )

        ease_of_navigation = st.radio(
            'How easy was it to navigate our website?',
            ['Very Difficult', 'Difficult', 'Neutral', 'Easy', 'Very Easy']
        )

        content_relevance = st.radio(
            'How relevant was the content on our website to your needs?',
            ['Not Relevant', 'Slightly Relevant', 'Moderately Relevant', 'Very Relevant', 'Extremely Relevant']
        )

        visual_appeal = st.radio(
            'How visually appealing did you find our website?',
            ['Not Appealing', 'Slightly Appealing', 'Moderately Appealing', 'Very Appealing', 'Extremely Appealing']
        )

        comments = st.text_area('Additional Comments or Suggestions', key='comments')

        # Submit Button
        submit_button = st.form_submit_button(label='Submit', help='Click to submit your feedback')

        if submit_button:
            if not name.strip() or not email.strip() or not phone_number.strip() or experience_rating is None:
                st.error("Please complete all required fields before submitting.")
            elif '@' not in email or '.' not in email.split('@')[-1]:
                st.error("Please enter a valid email address.")
            else:
                feedback = {
                    "Name": name,
                    "Email": email,
                    "Phone Number": phone_number,
                    "Experience Rating": experience_rating,
                    "Ease of Navigation": ease_of_navigation,
                    "Content Relevance": content_relevance,
                    "Visual Appeal": visual_appeal,
                    "Comments": comments
                }
                # Save feedback or send it to a database
                st.success("Thank you for your feedback! Your responses have been recorded.")
                st.json(feedback)  # Display the feedback in JSON format for visibility

if __name__ == "__main__":
    main()
