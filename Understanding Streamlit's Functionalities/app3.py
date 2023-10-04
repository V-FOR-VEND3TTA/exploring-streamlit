"""
Reading and displaying contents of a file
"""
import streamlit as st
# import the library that deals with data
import pandas as pd

# store the file that will be displayed in a variable
df = pd.read_csv('fixed_fb_data.csv')

# write to the app
st.write(df)

