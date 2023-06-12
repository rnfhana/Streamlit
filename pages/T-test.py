import streamlit as st
import pandas as pd
from statistics import NormalDist
from scipy.stats import ttest_1samp
import math

st.write('## Input Data')

data = st.text_area("Input data (pisahkan dengan koma)", value="")

# Memisahkan data yang dimasukkan
data_list = [float(x.strip()) for x in data.split(",") if x.strip() != ""]

if not data_list:
    st.warning("Input at least one data")
else:
    df = pd.DataFrame({'Data': data_list})

    with st.expander("View Data"):
        st.dataframe(df.transpose())

    with st.expander("View Statistics"):
        st.dataframe(df.describe())

    st.write('## Estimate The Average')

    alpha = 0.05
    alpha_t = NormalDist().inv_cdf(p=1 - alpha / 2)

    sample_mean = df['Data'].mean()
    sample_std = df['Data'].std()
    sample_size = len(df['Data'])

    margin_error = alpha_t * (sample_std / math.sqrt(sample_size))

    confidence_interval = (sample_mean - margin_error, sample_mean + margin_error)

    clicked = st.button('View Estimation')

    if clicked:
        st.write("Sample Mean:", sample_mean)
        st.write("Sample Standard Deviation :", sample_std)
        st.write("Sample Size:", sample_size)
        st.write("Margin of Error:", margin_error)
        st.write("Confidence Interval 95%:", confidence_interval)

    st.write('## Constructing Hypothesis')

    alpha = 0.05
    null_mean = 67.5

    t_statistic, p_value = ttest_1samp(df['Data'], null_mean)

    clicked = st.button('Do the t-test!!')

    if clicked:
        alpha_t = alpha / 2
        if p_value < alpha and sample_mean > null_mean:
            st.write('Reject H0. The sample mean is significantly greater than', null_mean)
        elif p_value < alpha and sample_mean < null_mean:
            st.write('Reject H0. The sample mean is significantly less than', null_mean)
        else:
            st.write('Cannot reject H0. The sample mean is not significantly different from', null_mean)

        st.write('t-statistic:', t_statistic)
        st.write('p-value:', p_value)
