import streamlit as st

# Stream UI

st.title("Power calulcator")
st.write("Enter a number to calculate its square")


# Get user input
n=st.number_input("Ënter an integer", value=1, step=1)


# Calculate results

square= n**2
cube=n**3
fifth_power= n**5


# Display results
st.write(f"THe number of {n}:{square}")
st.write(f"THe cube of {n}:{cube}")
st.write(f"THe fifth power of {n}:{fifth_power}")