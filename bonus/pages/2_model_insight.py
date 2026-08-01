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
col1.metric("Adjusted R²", "0.5779", delta="+0.048")
col2.metric("RMSE", "19.05", delta="-1.13")
col3.metric("Countries", "133")

# feature impact
st.subheader("Feature Impact")

features = ["Rural Population", "Gov Health Exp", "GDP per Capita", "GDP²"]
importance = [-8.48, 5.12, 3.99, -0.0001]
colors = ["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff"]

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
- **GDP per capita** is the strongest predictor (wealth → better access)
- The relationship is **non-linear**: adding GDP² improved the model
- **Rural population** reduces water access
- **Government health spending** has a positive but weaker effect
""")