import streamlit as st

# Custom styling and title
st.markdown("""
    <style>
        .custom-title {
            font-size: 2em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Display the custom image and title
st.image("https://link-to-your-image.png", width=200)  # Replace with your working image URL
st.markdown('<div class="custom-title">TruthSeeker AI</div>', unsafe_allow_html=True)
