import streamlit as st
import json
import os

# Path to store responses
RESPONSES_FILE = 'survey_responses.json'

def save_response(response):
    if os.path.exists(RESPONSES_FILE):
        with open(RESPONSES_FILE, 'r') as file:
            responses = json.load(file)
    else:
        responses = []
    
    responses.append(response)
    
    with open(RESPONSES_FILE, 'w') as file:
        json.dump(responses, file, indent=4)

def main():
    st.title('Household Energy Consumption Survey')

    with st.form(key='survey_form'):
        # Section 0: Contact Information
        st.header('Section 0: Contact Information')

        name = st.text_input('Name', key='name')
        email = st.text_input('Email', key='email')
        phone_number = st.text_input('Phone Number', key='phone_number')

        # Initialize session state variables
        if 'using_smart_devices' not in st.session_state:
            st.session_state.using_smart_devices = 'No'
        if 'received_incentives' not in st.session_state:
            st.session_state.received_incentives = 'No'

        # Section 1: Demographic Information
        st.header('Section 1: Demographic Information')

        household_size = st.selectbox(
            'How many people live in your household?',
            ['Choose an option', '1-2', '3-4', '5-6', '7+'],
            key='household_size'
        )

        age_group = st.selectbox(
            'What is your age group?',
            ['Choose an option', '18-24', '25-34', '35-44', '45-54', '55+'],
            key='age_group'
        )

        electricity_bill = st.selectbox(
            'What is your average monthly electricity bill?',
            ['Choose an option', 'Less than Rs.1000', 'Rs.1000-Rs.3000', 'Rs.3000-Rs.5000', 'More than Rs.5000'],
            key='electricity_bill'
        )

        # Section 2: Energy Consumption Patterns
        st.header('Section 2: Energy Consumption Patterns')

        electricity_use_time = st.multiselect(
            'When do you use the most electricity at home? (Select all that apply)',
            ['Weekdays', 'Evenings', 'Weekends', 'Mornings', 'Nights'],
            key='electricity_use_time'
        )

        energy_sources = st.multiselect(
            'What are the primary sources of energy usage in your home? (Select all that apply)',
            ['Heating/Cooling', 'Lighting', 'Appliances (e.g., fridge, oven)', 'Electronics (e.g., TV, computer)', 'Water Heating'],
            key='energy_sources'
        )

        energy_practices = st.selectbox(
            'How often do you perform energy-efficient practices, such as turning off lights or unplugging devices when not in use?',
            ['Choose an option', 'Never', 'Rarely', 'Sometimes', 'Often', 'Always'],
            key='energy_practices'
        )

        appliance_efficiency = st.selectbox(
            'How energy-efficient do you consider your current appliances to be?',
            ['Choose an option', 'Very Inefficient', 'Somewhat Inefficient', 'Neutral', 'Somewhat Efficient', 'Very Efficient'],
            key='appliance_efficiency'
        )

        # Section 3: Technology and Monitoring
        st.header('Section 3: Technology and Monitoring')

        using_smart_devices = st.radio(
            'Are you currently using any smart devices for energy monitoring?',
            ['Yes', 'No'],
            index=0,  # Default to 'Yes'
            key='using_smart_devices'
        )

        # Use a placeholder to conditionally render smart devices question
        if st.session_state.using_smart_devices == 'Yes':
            smart_devices = st.multiselect(
                'If yes, which smart devices do you use for energy monitoring? (Select all that apply)',
                ['Smart Thermostat', 'Smart Plugs', 'Energy Monitoring Apps', 'Other (please specify)'],
                key='smart_devices'
            )
        else:
            smart_devices = []

        interest_in_data = st.selectbox(
            'How interested are you in receiving real-time energy consumption data and personalized recommendations to optimize usage?',
            ['Choose an option', 'Not Interested', 'Slightly Interested', 'Moderately Interested', 'Very Interested', 'Extremely Interested'],
            key='interest_in_data'
        )

        # Section 4: Behavioral Insights and Barriers
        st.header('Section 4: Behavioral Insights and Barriers')

        barriers = st.multiselect(
            'What barriers do you face in implementing energy-saving measures? (Select all that apply)',
            ['Lack of information', 'Cost of upgrades', 'Inconvenience', 'Lack of motivation', 'Other (please specify)'],
            key='barriers'
        )

        received_incentives = st.radio(
            'Have you ever received incentives for reducing energy consumption?',
            ['Yes', 'No'],
            index=0,  # Default to 'Yes'
            key='received_incentives'
        )

        # Use a placeholder to conditionally render incentives question
        if st.session_state.received_incentives == 'Yes':
            incentives = st.multiselect(
                'If yes, what type of incentives would motivate you to reduce energy consumption? (Select all that apply)',
                ['Discounts on energy bills', 'Cash rewards', 'Recognition or awards', 'Tax credits', 'Other (please specify)'],
                key='incentives'
            )
        else:
            incentives = []

        # Submit Button
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            # Validate that all required fields are filled
            if (name == '' or 
                email == '' or 
                phone_number == '' or 
                household_size == 'Choose an option' or 
                age_group == 'Choose an option' or 
                electricity_bill == 'Choose an option' or 
                not electricity_use_time or 
                not energy_sources or 
                energy_practices == 'Choose an option' or 
                appliance_efficiency == 'Choose an option' or 
                not barriers or 
                (st.session_state.using_smart_devices == 'Yes' and not smart_devices) or 
                (st.session_state.received_incentives == 'Yes' and not incentives)):
                
                st.error("Please complete all required fields before submitting.")
            else:
                response = {
                    "Name": name,
                    "Email": email,
                    "Phone Number": phone_number,
                    "Household Size": household_size,
                    "Age Group": age_group,
                    "Electricity Bill": electricity_bill,
                    "Electricity Use Time": electricity_use_time,
                    "Energy Sources": energy_sources,
                    "Energy Practices": energy_practices,
                    "Appliance Efficiency": appliance_efficiency,
                    "Using Smart Devices": st.session_state.using_smart_devices,
                    "Smart Devices": smart_devices,
                    "Interest in Data": interest_in_data,
                    "Barriers": barriers,
                    "Received Incentives": st.session_state.received_incentives,
                    "Incentives": incentives
                }

                save_response(response)
                
                st.success("Thank you for participating in the survey! Your responses have been recorded.")

if __name__ == "__main__":
    main()
