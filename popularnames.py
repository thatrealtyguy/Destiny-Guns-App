import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Welcome to my popular names app!

"""
names = pd.read_csv('popular_names.csv')
names['sex'] = names['sex'].astype(str)
names['year'] = names['year'].astype(int)
genders = ['M', 'F']

old_name = ""
old_gender = ""

user_name = st.text_input("Enter name here")
user_gender = st.selectbox("Select gender", genders)
min_year = st.slider("Starting year", 1910, 2021, 1910)
max_year = st.slider("Ending year", 1910, 2021, 2021)

# Filter data based on user input (assuming 'name' is a column in 'data')
if user_name != old_name or user_gender != old_gender:  # Check if the name has changed
  old_name = user_name  # Update old_name for future comparisons
  old_gender = user_gender  # Update old_gender for future comparisons
  filtered_data = names[names['name'] == user_name]
  filtered_data = filtered_data[filtered_data['sex'] == user_gender]

  # Check if data was found
  if not filtered_data.empty:
    plt.style.use('dark_background')
    # Create the line plot (with additional considerations for Streamlit)
    fig, ax = plt.subplots()  # Create a figure and axis for better control
    plt.plot(filtered_data['year'], filtered_data['n'], color = 'tomato')

    # Customize the plot (optional)
    plt.xlim(min_year, max_year)
    ax.set_title('Popularity Over Time for ' + user_name)
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    ax.grid()

    # Display the plot in Streamlit
    st.pyplot(fig)
  else:
    # Display a message if no data found for the entered name
    st.warning("No data found for the entered name.")
else:
  # Name hasn't changed, so don't refilter or display plot again
  pass  # Do nothing (avoids unnecessary computations and plot updates)

# Display message if no name was entered
if not user_name:
  st.warning("Please enter a name.")
