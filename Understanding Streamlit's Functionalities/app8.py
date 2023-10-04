"""
Dropdown options - multiple and single selection options using Streamlit
"""

import streamlit as st
import pandas as pd

# single select dropdown
lang = st.selectbox("Which programming language are you most familiar with?", ['Python', 'JavaScript', 'Ruby', 'Java', 'R', 'C++', 'Go'])
st.write("The programming language you are most familiar with is", lang)

# multi select dropdown
langs = st.multiselect("Which are the programming languages you know?", ['Python', 'JavaScript', 'Ruby', 'Java', 'R', 'C++', 'Go'])
st.write("Number of programming languages you know is", len(langs))

