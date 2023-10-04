"""
Using the submit button, selection box, and sliders in streamlit
"""

import streamlit as st
import pandas as pd

# Selection Box
specialization = st.selectbox('Select Specialization', ['Machine Learning', 'Deep Learning'])
st.write("Your specialization is", specialization)

# The Submit Button
with st.form(key='my_form'):
	text_input = st.text_input(label='Enter your name')
	submit_button = st.form_submit_button(label='Submit')

# The slider functionality
col1, col2 = st.columns(2)

with col1:
    with st.form('Form1'):
        st.selectbox('Select Role', ['Development', 'Business Analysis'], key=1)
        st.slider(label='Select knowledge level', min_value=0, max_value=10, key=4)
        submitted1 = st.form_submit_button('Submit 1')
        
        if submitted1:
            st.success('Form 1 Submitted Successfully!')

with col2:
    with st.form('Form2'):
        st.selectbox('Select Algorithm', ['Logistic', 'Random Forest'], key=2)
        st.slider(label='Select knowledge level', min_value=0, max_value=10, key=3)
        submitted2 = st.form_submit_button('Submit 2')
        
        if submitted2:
            st.success('Form 2 Submitted Successfully!')
