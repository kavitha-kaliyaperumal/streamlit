import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Simple Streamlit App")

# Slider widget to select a number
num = st.slider("Pick a number", min_value=1, max_value=100, value=50)

# Generate some data based on the selected number
x = np.linspace(0, 10, num)
y = np.sin(x)

# Display a plot of the sine wave
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
st.pyplot(fig)

# Displaying text input
user_input = st.text_input("What’s your favorite programming language?", "Python")
st.write(f"Your favorite programming language is {user_input}!")

# Dataframe display
df = pd.DataFrame({
    'X': x,
    'Y': y
})
st.write(df)

