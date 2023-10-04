# import streamlit with an alias
import streamlit as st

# define the text we want to display
st.text("Hello World")

# show the text we want to display as a paragraph
original_title = '<p style="font-family: Courier; color: blue; font-size: 20px;">Hello World</p>'
st.markdown(original_title, unsafe_allow_html=True)

# show the text we want to display as a paragraph in another text format (md)
new_title = '<p style="font-family: sans-serif; color: green; font-size: 42px;">Hello World</p>'
st.markdown(new_title, unsafe_allow_html=True)
