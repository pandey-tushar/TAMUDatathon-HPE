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

st.write(
    "Let's filter the data: "
    )

st.write(df[["State", "Geographic School District", "% Poverty (SAIPE Estimate)"]])
