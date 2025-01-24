import streamlit as st

# Title of the app
st.title("Simple Streamlit Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Dropdown to select the operation
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation based on selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero!"

# Display the result
st.write(f"The result of {operation}ing {num1} and {num2} is: {result}")
