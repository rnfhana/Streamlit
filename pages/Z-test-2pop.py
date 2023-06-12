import streamlit as st
import pandas as pd
from statistics import NormalDist
from statsmodels.stats.weightstats import ztest
import math

st.write('## Input Data')

data1 = st.text_area("Data Populasi 1 (pisahkan dengan koma)", value="")
data2 = st.text_area("Data Populasi 2 (pisahkan dengan koma)", value="")

# Memisahkan data yang dimasukkan
data_list1 = [float(x.strip()) for x in data1.split(",") if x.strip() != ""]
data_list2 = [float(x.strip()) for x in data2.split(",") if x.strip() != ""]

if not data_list1 or not data_list2:
    st.warning("Input at least one data for each population")
else:
    df1 = pd.DataFrame({'Data': data_list1})
    df2 = pd.DataFrame({'Data': data_list2})

    with st.expander("View Data"):
        st.write("Population 1:")
        st.dataframe(df1.transpose())
        st.write("Population 2:")
        st.dataframe(df2.transpose())

    with st.expander("View Statistics"):
        st.write("Population 1:")
        st.dataframe(df1.describe())
        st.write("Population 2:")
        st.dataframe(df2.describe())

    st.write('## Perform Two-Sample Z-Test')

    alpha = 0.05
    alpha_z = NormalDist().inv_cdf(p=1 - alpha / 2)

    sample_mean1 = df1['Data'].mean()
    sample_std1 = df1['Data'].std()
    sample_size1 = len(df1['Data'])

    sample_mean2 = df2['Data'].mean()
    sample_std2 = df2['Data'].std()
    sample_size2 = len(df2['Data'])

    z_score, p_value = ztest(df1['Data'], df2['Data'])

    clicked = st.button('Do the Z-Test!!')

    if clicked:
        st.write("Population 1:")
        st.write("Sample Mean:", sample_mean1)
        st.write("Sample Standard Deviation:", sample_std1)
        st.write("Sample Size:", sample_size1)

        st.write("Population 2:")
        st.write("Sample Mean:", sample_mean2)
        st.write("Sample Standard Deviation:", sample_std2)
        st.write("Sample Size:", sample_size2)

        st.write("Z-Score:", z_score)
        st.write("p-value:", p_value)

        if abs(z_score) > alpha_z:
            st.write("Reject H0. The means of two populations are significantly different.")
        else:
            st.write("Cannot reject H0. The means of two populations are not significantly different.")

    clicked = st.button('View Estimation')

    if clicked:
        st.write('## Estimate of Population Means')

        margin_error1 = alpha_z * (sample_std1 / math.sqrt(sample_size1))
        confidence_interval1 = (sample_mean1 - margin_error1, sample_mean1 + margin_error1)
        st.write("Population 1:")
        st.write("Estimate of Mean:", sample_mean1)
        st.write("Margin of Error:", margin_error1)
        st.write("Confidence Interval 95%:", confidence_interval1)

        margin_error2 = alpha_z * (sample_std2 / math.sqrt(sample_size2))
        confidence_interval2 = (sample_mean2 - margin_error2, sample_mean2 + margin_error2)
        st.write("Population 2:")
        st.write("Estimate of Mean:", sample_mean2)
        st.write("Margin of Error:", margin_error2)
        st.write("Confidence Interval 95%:", confidence_interval2)
