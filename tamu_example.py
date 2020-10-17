# TAMU Datathon - HPE Challenge

# Playing around with streamlit

import streamlit as st
import numpy as np
import pandas as pd

st.title("TAMU Datathon")

df = pd.read_excel("https://urban-data-catalog.s3.amazonaws.com/drupal-root-live/2020/06/08/NHGIS_District_data.xlsx")

st.write(
    "Here is the data: "
    )
st.write(df)

# Try out filtering the data and using a checkbox

st.write("Filter the data: ")

if st.checkbox("Poverty"):
    st.write(df[["State", "Geographic School District", "% Poverty (SAIPE Estimate)"]])
elif st.checkbox("Internet/Computer Access"):
    st.write(df[["State", "Geographic School District", "% No Computer or Internet Estimate"]])
elif st.checkbox("Vulnerable Jobs"):
    st.write(df[["State", "Geographic School District", "% HHs With Vulnerable Job Estimate"]])
elif st.checkbox("Single Parent Houshold"):
    st.write(df[["State", "Geographic School District", "% Single Parent Estimate"]])

# Filter by state
# working on this
