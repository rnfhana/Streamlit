import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import linregress

st.write('## Input Data')

data_x = st.text_area("Input data X (pisahkan dengan koma)", value="")
data_y = st.text_area("Input data Y (pisahkan dengan koma)", value="")

# Memisahkan data yang dimasukkan
data_list_x = [float(x.strip()) for x in data_x.split(",") if x.strip() != ""]
data_list_y = [float(y.strip()) for y in data_y.split(",") if y.strip() != ""]

if not data_list_x or not data_list_y:
    st.warning("Input at least one data for X and Y")
else:
    df = pd.DataFrame({'X': data_list_x, 'Y': data_list_y})

    with st.expander("View Data"):
        st.dataframe(df)

    with st.expander("View Statistics"):
        st.dataframe(df.describe())

    st.write('## Correlation Coefficient')

    x = df['X']
    y = df['Y']

    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    clicked = st.button('Perform Correlation Coefficient')

    if clicked:
        st.write("Correlation Coefficient (R):", r_value)
        st.write("R-squared:", r_value**2)

    st.write('## Perform Linear Regression')

    clicked = st.button('Perform Linear Regression')

    if clicked:
        st.write("Slope:", slope)
        st.write("Intercept:", intercept)
        st.write("R-value:", r_value)
        st.write("P-value:", p_value)
        st.write("Standard Error:", std_err)

        


