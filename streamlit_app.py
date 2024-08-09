import streamlit as st
from openai import OpenAI

# Set up the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["api_keys"]["openai_api_key"]

# Show custom title and logo
st.markdown("""
    <style>
        .reportview-container {
            background: #f0f0f0;
        }
        header {
            visibility: hidden;
        }
        .stApp {
            background-color: #f7f7f7;
            padding-top: 10px;
        }
        .custom-title {
            font-size: 2em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            padding: 10px;
            margin-bottom: 10px;
        }
        .custom-chatbox {
            font-size: 1.2em;
            font-weight: bold;
            color: #333333;
            padding: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Display the custom image and title
st.image("https://chatgpt.com/g/g-sSJGOf9Rb-truthseeker-ai.png", width=200)  # Replace with your image URL
st.markdown('<div class="custom-title">TruthSeeker AI</div>', unsafe_allow_html=True)

# Introduction text
st.write("Welcome to TruthSeeker AI! Ask any question related to Jehovah's Witnesses' teachings, and I will provide answers based on the New World Translation of the Holy Scriptures.")

# Ensure the API key is available
if not openai_api_key:
    st.error("OpenAI API key not found. Please configure it in the secrets management.", icon="⚠️")
else:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message.
    if prompt := st.chat_input("Enter your question below:"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API with GPT-4.
        stream = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Optional: Display a footer
st.write("Powered by GPT-4 | Built with Streamlit")
