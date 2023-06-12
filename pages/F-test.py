import streamlit as st
import pandas as pd
from statistics import variance
from scipy.stats import f

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

    st.write('## Perform F-Test')

    sample_variance1 = variance(df1['Data'])
    sample_size1 = len(df1['Data'])

    sample_variance2 = variance(df2['Data'])
    sample_size2 = len(df2['Data'])

    f_value = sample_variance1 / sample_variance2
    degrees_of_freedom1 = sample_size1 - 1
    degrees_of_freedom2 = sample_size2 - 1
    p_value = f.cdf(f_value, degrees_of_freedom1, degrees_of_freedom2)

    clicked = st.button('Do the F-Test!!')

    if clicked:
        st.write("Population 1:")
        st.write("Sample Variance:", sample_variance1)
        st.write("Sample Size:", sample_size1)

        st.write("Population 2:")
        st.write("Sample Variance:", sample_variance2)
        st.write("Sample Size:", sample_size2)

        st.write("F-Value:", f_value)
        st.write("p-value:", p_value)

        alpha = 0.05

        if p_value < alpha:
            st.write("Reject H0. The variances of two populations are significantly different.")
        else:
            st.write("Cannot reject H0. The variances of two populations are not significantly different.")

    clicked = st.button('View Estimation')

    if clicked:
        st.write('## Estimate of Population Variances')

        st.write("Population 1:")
        st.write("Estimate of Variance:", sample_variance1)

        st.write("Population 2:")
        st.write("Estimate of Variance:", sample_variance2)

        st.write('## Estimate of Population Mean')

        st.write("Population 1:")
        mean_estimate1 = df1['Data'].mean()
        st.write("Estimate of Mean:", mean_estimate1)

        st.write("Population 2:")
        mean_estimate2 = df2['Data'].mean()
        st.write("Estimate of Mean:", mean_estimate2)
