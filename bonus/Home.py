import streamlit as st

st.set_page_config(
    page_title="Home"
)

st.write("""
# Welcome to Water Access Predictor

In this project, you can predict a country's safe drinking water access rate using economic and demographic indicators.

To get started:
1. Click the **Predict** page and enter the country's GDP, rural population, and government health expenditure.
1. Click the **Predict** button to get the predicted water access rate.
1. Click the **Data Insights** page to view model performance and key findings.
""")

st.write("**Data Source**: World Bank Open Data (2023)")