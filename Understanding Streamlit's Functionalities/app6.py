"""
How to upload a file in streamlit
"""

import streamlit as st
import pandas as pd

file_bytes = st.file_uploader("Upload a file (CSV only)", type="csv")
