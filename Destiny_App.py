import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Welcome to my Destiny 2 guns app!

"""
st.markdown("""
This app is based on data from [Destiny Tracker](https://destinytracker.com/destiny-2/db/items/weapon).
""")
st.markdown("""
Data is from before "Into the Light" expansion.
""")

guns = pd.read_csv('Destiny_Guns.csv')
elements = ['Kinetic', 'Solar', 'Void', 'Arc', 'Stasis', 'Strand']
types = ['Sword', 'Sidearm', 'Glaive', 'Shotgun', 'Hand Cannon',
        'Scout Rifle', 'Auto Rifle', 'Pulse Rifle', 'Submachine Gun',
        'Combat Bow', 'Fusion Rifle', 'Sniper Rifle', 'Trace Rifle',
        'Grenade Launcher', 'Machine Gun', 'Rocket Launcher',
        'Linear Fusion Rifle']
rarities = ['Common', 'Uncommon','Rare','Legendary','Exotic']
graphs = ['Box Plot', 'Scatter Plot', 'Bar Chart']
num_features = ['Impact', 'Range', 'RPM', 'Magazine']
cat_features = ['Element', 'Type', 'Rarity']
color_features = ['None', 'Element', 'Type', 'Rarity']

old_graph = ""
old_x = ""
old_y = ""
old_color = ""

user_graph = st.selectbox("Select Graph Type", graphs)

if user_graph != old_graph:
  old_graph = user_graph # Update old_graph for future comparisons

  if user_graph == 'Box Plot':
    user_x_var = st.selectbox("Select Categorical Variable for the X Axis", cat_features)
    user_y_var = st.selectbox("Select Numerical Variable for the Y Axis", num_features)

    if user_x_var != old_x or user_y_var != old_y:
      old_x = user_x_var
      old_y = user_y_var

      plt.style.use('dark_background')
      # Create the box plot (with additional considerations for Streamlit)
      fig = px.box(guns, x=user_x_var, y=user_y_var)

      # Customize the plot
      fig.update_layout(title = 'Boxplot for ' + user_x_var + ' by ' + user_y_var)

      # Display the plot in Streamlit
      st.plotly_chart(fig)

  elif user_graph == 'Scatter Plot':
    user_x_var = st.selectbox("Select Numerical Variable for the X Axis", num_features)
    user_y_var = st.selectbox("Select Numerical Variable for the Y Axis", num_features)

    if user_x_var == user_y_var:
      st.warning("You chose 2 of the same variable. Scatter Plot unavailable.")
    elif user_x_var != old_x or user_y_var != old_y:
      old_x = user_x_var
      old_y = user_y_var

      plt.style.use('dark_background')
      # Create the box plot (with additional considerations for Streamlit)
      fig = px.scatter(guns, x=user_x_var, y=user_y_var)

      # Customize the plot
      fig.update_layout(title = 'Scatterplot for ' + user_x_var + ' by ' + user_y_var)

      # Display the plot in Streamlit
      st.plotly_chart(fig)

  elif user_graph == 'Bar Chart':
    user_x_var = st.selectbox("Select Categorical Variable for the X Axis", cat_features)
    user_color_var = st.selectbox("OPTIONAL: Select Categorical Variable for coloring", color_features)

    if old_x != user_x_var or old_color != user_color_var:
      old_x = user_x_var
      if user_color_var != "None":
        old_color = user_color_var

        guns_counts = guns.groupby(['Element', 'Type', 'Rarity']).size().to_frame(name='Count').reset_index()

        plt.style.use('dark_background')
        # Create the box plot (with additional considerations for Streamlit)
        fig = px.bar(guns_counts, x=user_x_var, y='Count', color = user_color_var)

        # Customize the plot
        fig.update_layout(title = 'Bar Chart for ' + user_x_var + ' and colored by ' + user_color_var)

        # Display the plot in Streamlit
        st.plotly_chart(fig)
      
      else:
        old_color = user_color_var
        
        guns_counts = guns.groupby(['Element', 'Type', 'Rarity']).size().to_frame(name='Count').reset_index()

        plt.style.use('dark_background')
        # Create the box plot (with additional considerations for Streamlit)
        fig = px.bar(guns_counts, x=user_x_var, y='Count')

        # Customize the plot
        fig.update_layout(title = 'Bar Chart for ' + user_x_var)

        # Display the plot in Streamlit
        st.plotly_chart(fig)

# Display message if no graph was chosen
if not user_graph:
  st.warning("Please choose a graph.")

st.markdown("""
* This app is based on the code available on [GitHub](https://github.com/thatrealtyguy/Destiny-Guns-App).
""")