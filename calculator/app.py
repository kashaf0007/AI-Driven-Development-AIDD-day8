
import streamlit as st

st.title("🔢 Simple Calculator")

num1 = st.number_input("Enter First Number", value=0)
num2 = st.number_input("Enter Second Number", value=0)

operation = st.selectbox(
    "Select Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = "Error! Division by zero." if num2 == 0 else num1 / num2

    st.success(f"Result: {result}")
