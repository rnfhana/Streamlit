import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import chi2, chi2_contingency
from statistics import variance

st.write('## Input Data')

data = st.text_area("Input data (pisahkan dengan koma)", value="")

# Memisahkan data yang dimasukkan
data_list = [x.strip() for x in data.split(",") if x.strip() != ""]

if not data_list:
    st.warning("Input at least one data")
else:
    df = pd.DataFrame({'Data': data_list})

    with st.expander("View Data"):
        st.dataframe(df.transpose())

    with st.expander("View Statistics"):
        st.dataframe(df.describe())

    st.write('## Estimate The Variance')

    # Mengonversi data ke dalam tipe numerik
    df['Data'] = pd.to_numeric(df['Data'], errors='coerce')

    sample_variance = variance(df['Data'])
    sample_size = len(df['Data'])
    degrees_of_freedom = sample_size - 1

    chi2_alpha = chi2.ppf(0.025, degrees_of_freedom)
    chi2_beta = chi2.ppf(0.975, degrees_of_freedom)

    interval_lower = (sample_size - 1) * sample_variance / chi2_beta
    interval_upper = (sample_size - 1) * sample_variance / chi2_alpha

    clicked = st.button('View Estimation')

    if clicked:
        st.write("Sample Variance:", sample_variance)
        st.write("Sample Size:", sample_size)
        st.write("Degrees of Freedom:", degrees_of_freedom)
        st.write("Interval Lower:", interval_lower)
        st.write("Interval Upper:", interval_upper)

    st.write('## Perform Chi-Square Test')

    chi2_statistic, p_value, _, _ = chi2_contingency(pd.crosstab(index=df['Data'], columns='count'))

    clicked = st.button('Do the Chi-Square Test!!')

    if clicked:
        st.write('Chi-Square:', chi2_statistic)
        st.write('p-value:', p_value)

        alpha = 0.05

        if p_value < alpha:
            st.write('Reject H0. The data suggests a significant association.')
        else:
            st.write('Cannot reject H0. The data does not suggest a significant association.')
