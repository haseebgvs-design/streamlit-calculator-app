import streamlit as st

# App title
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")

st.write("Enter numbers and choose an operation below:")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"The result of division is: {result}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
