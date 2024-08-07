# import streamlit as st
# import google.generativeai as genai

# # Configure the API key
# GOOGLE_API_KEY = "AIzaSyDma9KsEXzewUDnLTErjwVIyR3qwcRVlD8"
# genai.configure(api_key=GOOGLE_API_KEY)

# # Initialize the Generative Model
# model = genai.GenerativeModel('gemini-pro')

# # Function to get response from the model
# def get_chatbot_response(user_input):
#     response = model.generate_content(user_input)
#     return response.text

# # Streamlit interface
# st.set_page_config(page_title="Simple ChatBot", page_icon=":robot:", layout="centered")

# st.title("✨ Simple ChatBot ✨")
# st.write("Powered by Google Generative AI")

# # Initialize session state for chat history
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Display chat history
# for user_message, bot_message in st.session_state.history:
#     st.markdown(f"""
#     <div style="
#         background-color: #d1d3e0; 
#         border-radius: 15px; 
#         padding: 10px 15px; 
#         margin: 5px 0; 
#         max-width: 70%; 
#         text-align: left; 
#         display: inline-block;
#     ">
#         <p style="margin: 0; font-size: 16px; line-height: 1.5;">{user_message}</p>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown(f"""
#     <div style="
#         background-color: #e1ffc7; 
#         border-radius: 15px; 
#         padding: 10px 15px; 
#         margin: 5px 0; 
#         max-width: 70%; 
#         text-align: left; 
#         display: inline-block;
#     ">
#         <p style="margin: 0; font-size: 16px; line-height: 1.5;">{bot_message}</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Input field at the bottom
# user_input = st.text_input("You: ", "", max_chars=500)

# if st.button("Send"):
#     if user_input:
#         response = get_chatbot_response(user_input)
#         st.session_state.history.append((user_input, response))
#         # Clear the input field after sending
#         st.text_input("You: ", "", max_chars=500, key="new_input")
#     else:
#         st.warning("Please enter a message.")


import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "AIzaSyDma9KsEXzewUDnLTErjwVIyR3qwcRVlD8"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro')

# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="Simple ChatBot", page_icon=":robot:", layout="centered")

st.title("✨ Simple ChatBot ✨")
st.write("Powered by Google Generative AI")

# Initialize session state for chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;">{user_message}</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div style="
        background-color: #e1ffc7; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;">{bot_message}</p>
    </div>
    """, unsafe_allow_html=True)

# Input field at the bottom
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You: ", "", max_chars=500)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please enter a message.")
