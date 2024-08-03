import streamlit as st

def main():
    st.title('Feedback Form')

    # Create a form for feedback submission
    with st.form(key='feedback_form'):
        # Personal Information
        st.header('Personal Information')

        name = st.text_input('Name')
        email = st.text_input('Email')
        phone_number = st.text_input('Phone Number')

        # User Experience
        st.header('User Experience')

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

        comments = st.text_area('Additional Comments or Suggestions')

        # Submit Button
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not name.strip() or not email.strip() or not phone_number.strip() or experience_rating is None:
                st.error("Please complete all required fields before submitting.")
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

if __name__ == "__main__":
    main()
