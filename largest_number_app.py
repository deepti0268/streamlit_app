import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

st.title("Find the Largest Number")

# Input fields for the three numbers
number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")
number3 = st.number_input("Enter the third number:")

# Find the largest number
largest_number = find_largest_number(number1, number2, number3)

# Display the result
st.write(f"The largest number is: {largest_number}")
