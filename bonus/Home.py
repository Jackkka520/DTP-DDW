import streamlit as st

st.set_page_config(
    page_title="Home"
)

st.write("""
# Welcome to Water Access Predictor

In this project, you can predict a country's safe drinking water access rate using economic and demographic indicators.

**Final Model**: Multiple Linear Regression with 2 predictors (GDP per capita (log) and rural population).

To get started:
1. Click the **Predict** page and enter the country's GDP and rural population.
1. Click the **Predict** button to get the predicted water access rate.
1. Click the **Data Insights** page to view model performance and key findings.
""")

st.write("**Data Source**: World Bank Open Data (2023)")