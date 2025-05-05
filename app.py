import streamlit as st

# Title of the app
st.title('Streamlit Demo App')

# Header for the input section
st.header('User Input')

# Text Input
user_name = st.text_input("Enter your name:")

# Number Input
age = st.number_input("Enter your age:", min_value=1, max_value=100)

# Button to submit the data
if st.button('Submit'):
    # Display Output based on user input
    st.write(f"Hello {user_name}, you are {age} years old!")
