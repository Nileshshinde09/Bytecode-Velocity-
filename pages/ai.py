'''
    This is a Python code that uses the Streamlit library to create a 
    simple web application, and the OpenAI API to generate responses to 
    user input. The function "aichat(ask)" takes in a user input "ask" 
    and sends it as a prompt to the OpenAI API, using the "text-davinci-003" 
    model. The API then generates a response, which is returned as "text". 
    The "ai()" function allows the user to input a question or command and 
    submit it to the "aichat(ask)" function. If the user inputs a question, 
    the returned response is displayed as markdown. If the user inputs a command,
     the returned response is displayed as code.


'''
import streamlit as st
import openai

# Set the OpenAI API key
openai.api_key =  st.secrets['KEY']

# Function to generate a response from the OpenAI API
def aichat(ask):
    try:
        # Send the user input as a prompt to the API
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            )

        # Get the generated response text
        text = response['choices'][0]['text']
        return text
    except Exception as e:
        st.error(e)

# Main function to handle user input and display the response
def ai():
    # Get user input for a question
    question = st.text_input("Ask Question :")
    # Submit button to send the question to the aichat function
    if st.button("Submit"):
        result = aichat(question)
        st.markdown(result)

    # Get user input for a command
    code = st.text_input("Give Command for write a code : ")
    # Submit button to send the command to the aichat function
    if st.button("Submit code",key ='code'):
        result = aichat(code)
        st.code(result) 
