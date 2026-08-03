# pages/Data_Insights.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Insights", layout="centered")
st.title("Model Insights")

# model performance
st.subheader("Performance")

col1, col2, col3 = st.columns(3)
col1.metric("Adjusted R²", "0.6768", delta="+0.2683")
col2.metric("RMSE", "15.80", delta="-5.13")
col3.metric("Countries", "133")

# feature impact
st.subheader("Feature Impact")

features = ["Rural Population", "log(GDP)"]
importance = [-3.31, 23.28]
colors = ["#ff6b6b", "#4d96ff"]

fig, ax = plt.subplots(figsize=(8, 3))
bars = ax.barh(features, importance, color=colors)
ax.axvline(x=0, color="black", linewidth=0.5)
ax.set_xlabel("Coefficient Value")
ax.set_title("Feature Impact on Water Access")

for bar, val in zip(bars, importance):
    ax.text(bar.get_width() + 0.1 if val > 0 else bar.get_width() - 0.3,
            bar.get_y() + bar.get_height()/2,
            f"{val:.2f}", va="center", ha="left" if val > 0 else "right")

st.pyplot(fig)

# key takeaways
st.subheader("Key Takeaways")
st.markdown("""
- **log(GDP)** is the strongest predictor (diminishing returns)
- **Rural population** reduces water access
- **Final model explains ~68% of variance** (Adjusted R² = 0.6768)
""")