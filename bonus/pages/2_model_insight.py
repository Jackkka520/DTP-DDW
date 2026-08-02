# pages/Data_Insights.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Insights", layout="centered")
st.title("Model Insights")

# model performance - UPDATED to log(GDP) model results
st.subheader("Performance")

col1, col2, col3 = st.columns(3)
col1.metric("Adjusted R²", "0.6601", delta="+0.2516")
col2.metric("RMSE", "15.87", delta="-5.06")
col3.metric("Countries", "133")

# feature impact - UPDATED coefficients for log(GDP) model
st.subheader("Feature Impact")

features = ["Rural Population", "Gov Health Exp", "log(GDP)"]
importance = [-10.10, 8.93, 8.78]
colors = ["#ff6b6b", "#ffd93d", "#4d96ff"]

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

# key takeaways - UPDATED
st.subheader("Key Takeaways")
st.markdown("""
- **log(GDP) replaced GDP²** — better captures the diminishing returns relationship
- **Adjusted R² improved from 0.4085 to 0.6601** (test set)
- **Rural population** reduces water access (strong negative effect)
- **Government health spending and GDP** both have positive effects
""")