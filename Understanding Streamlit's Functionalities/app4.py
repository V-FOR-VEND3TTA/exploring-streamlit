"""
How we create and display graphs in streamlit
"""
#the libraries we will need
import streamlit as st
import pandas as pd
import plotly.express as px

# the data we want to read
df = pd.read_csv('fixed_fb_data.csv')

st.write(df)

# create a graph with mobile app installs linked to the campaign that produced the result
graph = px.line(df, x='Campaign name', y='Mobile app installs')
st.plotly_chart(graph)

