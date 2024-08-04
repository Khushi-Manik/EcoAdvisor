import streamlit as st

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

# Custom CSS to style the app
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {background_color};
        }}
        .header {{
            background-color: {header_background_color};
            color: {header_text_color};  /* Ensures the header text is white */
            padding: 10px;
            border-radius: 5px;
        }}
        .header h1 {{
            color: {header_text_color}; /* Ensures the title text is white */
        }}
        .section {{
            background-color: {section_background_color};
            color: {section_text_color};  /* Text color inside green boxes */
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }}
        .section h2, .section h3, .section p, .section ul, .section li {{
            color: {section_text_color}; /* Ensures all nested elements have white text */
        }}
        .username {{
            color: {username_color};
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown('<div class="header"><h1>Energy Conservation Tips</h1></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    Welcome to the Energy Conservation Tips page! In this guide, we'll explore some easy and effective ways to save energy and reduce our environmental impact. Let's dive in!
</div>
""", unsafe_allow_html=True)

# Section 1: Why Conserve Energy?
st.markdown('<div class="section"><h2>1. Why Conserve Energy?</h2></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p>Conserving energy helps protect the environment, reduces energy bills, and conserves natural resources. By using less energy, we reduce the demand for fossil fuels, which lowers the amount of harmful emissions released into the atmosphere.</p>
</div>
""", unsafe_allow_html=True)

# Section 2: Simple Ways to Save Energy at Home
st.markdown('<div class="section"><h2>2. Simple Ways to Save Energy at Home</h2></div>', unsafe_allow_html=True)

# Subsection: Lighting
st.markdown('<div class="section"><h3>Lighting</h3></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ul>
        <li><strong>Use LED bulbs</strong>: They use up to 80% less energy and last longer than traditional bulbs.</li>
        <li><strong>Turn off lights when not in use</strong>: Simple and effective!</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Subsection: Appliances
st.markdown('<div class="section"><h3>Appliances</h3></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ul>
        <li><strong>Unplug devices</strong>: Many devices consume energy even when turned off. Unplug them when not in use.</li>
        <li><strong>Use energy-efficient appliances</strong>: Look for the ENERGY STAR label when buying new appliances.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Subsection: Heating and Cooling
st.markdown('<div class="section"><h3>Heating and Cooling</h3></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ul>
        <li><strong>Set your thermostat wisely</strong>: Lower it in winter and raise it in summer to save energy.</li>
        <li><strong>Use fans</strong>: They use less energy than air conditioners.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Section 3: Energy Conservation Tips for Businesses
st.markdown('<div class="section"><h2>3. Energy Conservation Tips for Businesses</h2></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ul>
        <li><strong>Implement energy-efficient lighting</strong>: Use LED lights and automatic timers.</li>
        <li><strong>Optimize HVAC systems</strong>: Regular maintenance and proper insulation can save energy.</li>
        <li><strong>Encourage telecommuting</strong>: Reduces energy usage in the office and cuts down on commuting.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Section 4: Renewable Energy Sources
st.markdown('<div class="section"><h2>4. Renewable Energy Sources</h2></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p>Consider using renewable energy sources like solar, wind, or hydropower to reduce dependence on fossil fuels.</p>
</div>
""", unsafe_allow_html=True)

# Section 5: Energy Conservation Tutorials
st.markdown('<div class="section"><h2>5. Energy Conservation Tutorials</h2></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    Here are some helpful YouTube tutorials on energy conservation:
    <ul>
        <li><a href="https://www.youtube.com/watch?v=example1" target="_blank">Energy Conservation Tips for Homeowners</a></li>
        <li><a href="https://www.youtube.com/watch?v=example2" target="_blank">Top 10 Ways to Save Energy</a></li>
        <li><a href="https://www.youtube.com/watch?v=example3" target="_blank">Energy Saving Tips for Small Businesses</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Conclusion
st.write("""
Thank you for exploring these energy conservation tips! By taking small steps, we can all make a big difference. Feel free to share your own tips and ideas in the comments below.
""")

# Interactive Elements
st.text_input("Your Energy Conservation Tips", "Share your tips here...")
st.button("Submit")