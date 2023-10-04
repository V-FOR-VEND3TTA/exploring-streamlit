"""
How to add a logo or image to your streamlit application 
"""
# the libraries we will need
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# the data we want to read
df = pd.read_csv('fixed_fb_data.csv')

st.write(df)

# create a graph with mobile app installs linked to the campaign that produced the result
graph = px.line(df, x='Campaign name', y='Mobile app installs')
st.plotly_chart(graph)

# the logo we want to use
image = Image.open('slytherin-emblem.png')
st.image(image, width=100)