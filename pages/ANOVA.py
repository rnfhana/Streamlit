import streamlit as st
import pandas as pd
import scipy.stats as stats

st.write('## Input Data')

data = []
num_populations = st.number_input("Number of Populations", min_value=2, value=2, step=1)

for i in range(num_populations):
    population_data = st.text_area(f"Data Populasi {i+1} (pisahkan dengan koma)", value="")
    population_list = [float(x.strip()) for x in population_data.split(",") if x.strip() != ""]
    data.append(population_list)

if not all(data):
    st.warning("Input data for each population")
else:
    dfs = []
    for i in range(num_populations):
        df = pd.DataFrame({'Data': data[i]})
        dfs.append(df)

    with st.expander("View Data"):
        for i in range(num_populations):
            st.write(f"Population {i+1}:")
            st.dataframe(dfs[i].transpose())

    with st.expander("View Statistics"):
        for i in range(num_populations):
            st.write(f"Population {i+1}:")
            st.dataframe(dfs[i].describe())

    st.write('## Perform ANOVA Test')

    f_stat, p_value = stats.f_oneway(*data)

    clicked = st.button('Do the ANOVA Test!!')

    if clicked:
        st.write("F-Statistic:", f_stat)
        st.write("p-value:", p_value)

        alpha = 0.05
        if p_value < alpha:
            st.write("Reject H0. There is a significant difference between the means of the populations.")
        else:
            st.write("Cannot reject H0. There is no significant difference between the means of the populations.")
