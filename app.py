import streamlit as st

# Title of the web app
st.title("Incident Management SLA predictor")

# Input boxes for user to enter five numbers
num1 = st.number_input("Enter number 1:")
num2 = st.number_input("Enter number 2:")
num3 = st.number_input("Enter number 3:")
num4 = st.number_input("Enter number 4:")
num5 = st.number_input("Enter number 5:")

operation = st.selectbox("Select operation for number 1", ["None", "Add", "Subtract", "Multiply", "Divide"])
operation2 = st.selectbox("Select operation for number 2", ["None", "Add", "Subtract", "Multiply", "Divide"])
operation3 = st.selectbox("Select operation for number 3", ["None", "Add", "Subtract", "Multiply", "Divide"])
operation4 = st.selectbox("Select operation for number 4", ["None", "Add", "Subtract", "Multiply", "Divide"])
operation5 = st.selectbox("Select operation for number 5", ["None", "Add", "Subtract", "Multiply", "Divide"])

# Function to calculate the square
def calculate_square(number):
    return number ** 2

# Check if the user has entered a number
if user_input:
    # Calculate the square
    result = calculate_square(user_input)
    st.write(f"The square of {user_input} is {result}")