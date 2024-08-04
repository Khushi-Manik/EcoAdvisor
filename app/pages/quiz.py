import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Energy Awareness Quiz", layout="wide")

# Define the color scheme
primary_green = "#1b4d3e"
darker_green = "#1c352d"
accent_green = "#014421"
background_color = "#FFFFFF"
header_background_color = darker_green
header_text_color = "#FFFFFF"
section_background_color = primary_green
section_text_color = "#FFFFFF"
username_color = primary_green
question_text_color = "#000000"  # Black color for question text

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
    .quiz-question {{
        margin-top: 20px;
        font-size: 1.2em;
        color: {question_text_color}; /* Set question text color to black */
    }}
    .quiz-option label {{
        color: {question_text_color}; /* Set option text color to black */
    }}
    .correct {{
        color: #4CAF50; /* Green color for correct answer */
        font-weight: bold;
    }}
    .incorrect {{
        color: #f44336; /* Red color for incorrect answer */
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header with title
st.markdown('<div class="stTitle">Energy Awareness Quiz</div>', unsafe_allow_html=True)

# Quiz questions and answers
quiz_questions = [
    {
        "question": "Which of the following is a common method to reduce household energy consumption?",
        "options": ["Using energy-efficient appliances", "Leaving lights on all day", "Taking long showers", "Keeping windows open in winter"],
        "answer": "Using energy-efficient appliances",
    },
    {
        "question": "What is the primary benefit of switching to LED light bulbs?",
        "options": ["Lower energy consumption", "Brighter light", "Cheaper purchase price", "Shorter lifespan"],
        "answer": "Lower energy consumption",
    },
    {
        "question": "How does turning off unused electrical devices help in energy conservation?",
        "options": ["Reduces standby power usage", "Increases device lifespan", "Enhances device performance", "None of the above"],
        "answer": "Reduces standby power usage",
    },
    {
        "question": "Why is it important to insulate your home properly?",
        "options": ["To prevent energy loss", "To improve indoor air quality", "To increase aesthetic appeal", "To reduce noise pollution"],
        "answer": "To prevent energy loss",
    },
    {
        "question": "What is a smart thermostat used for?",
        "options": ["Controlling home heating and cooling remotely", "Monitoring water usage", "Tracking electricity consumption", "Managing kitchen appliances"],
        "answer": "Controlling home heating and cooling remotely",
    },
    {
        "question": "Which practice helps in saving energy while cooking?",
        "options": ["Using a lid on pots and pans", "Keeping the oven door open", "Using multiple burners simultaneously", "Boiling water in a large pot"],
        "answer": "Using a lid on pots and pans",
    },
    {
        "question": "What is the main purpose of an energy audit?",
        "options": ["To assess energy consumption and identify savings", "To evaluate appliance performance", "To check for electrical safety", "To inspect home insulation"],
        "answer": "To assess energy consumption and identify savings",
    },
    {
        "question": "How can using energy-efficient windows impact your energy bills?",
        "options": ["By reducing heat loss in winter and heat gain in summer", "By increasing indoor lighting", "By lowering the cost of window installation", "By providing better views"],
        "answer": "By reducing heat loss in winter and heat gain in summer",
    },
    {
        "question": "Why is it beneficial to unplug devices when not in use?",
        "options": ["It prevents energy waste from standby power", "It improves device performance", "It extends the device’s warranty", "It reduces wear and tear on the device"],
        "answer": "It prevents energy waste from standby power",
    },
    {
        "question": "What is a common benefit of using programmable timers for home appliances?",
        "options": ["Automatic operation based on schedule", "Enhanced appliance features", "Lower initial cost", "Improved aesthetic appeal"],
        "answer": "Automatic operation based on schedule",
    },
]

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'score' not in st.session_state:
    st.session_state.score = 0

# Display questions and collect answers
for idx, question in enumerate(quiz_questions):
    st.markdown(
        f'<div class="quiz-question"><strong>Q{idx + 1}: {question["question"]}</strong></div>',
        unsafe_allow_html=True,
    )
    
    # Use radio button to select an answer
    selected_option = st.radio(
        "", question["options"], key=f'question_{idx}', label_visibility='collapsed'
    )
    st.session_state.responses[idx] = selected_option

# Submit button
if st.button("Submit Answers"):
    st.session_state.submitted = True
    st.session_state.score = 0
    for idx, question in enumerate(quiz_questions):
        if st.session_state.responses.get(idx) == question["answer"]:
            st.session_state.score += 1

# Display selected answers and final score
if st.session_state.submitted:
    for idx, question in enumerate(quiz_questions):
        st.markdown(
            f'<div class="quiz-question"><strong>Q{idx + 1}: {question["question"]}</strong></div>',
            unsafe_allow_html=True,
        )
        selected_option = st.session_state.responses.get(idx)
        st.markdown(
            f'<div class="quiz-option"><label>Selected: {selected_option}</label></div>',
            unsafe_allow_html=True,
        )
        if selected_option == question["answer"]:
            st.markdown('<div class="correct">Correct!</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="incorrect">Incorrect! The correct answer is: {question["answer"]}</div>',
                unsafe_allow_html=True,
            )
    
    if st.button("Show Score"):
        st.markdown(
            f'<div class="section"><h2>Your Score: {st.session_state.score}/{len(quiz_questions)}</h2></div>',
            unsafe_allow_html=True,
        )
        st.balloons()
