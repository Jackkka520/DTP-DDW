import streamlit as st
from library import predict_water_access, get_status
import pandas as pd

st.set_page_config(
    page_title="Water Access Predictor",
    layout="centered"
)

st.title("Water Access Predictor")
st.markdown("Enter a country's economic and demographic indicators to predict its safe drinking water access rate.")

# ---------- Initialize history ----------
if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("---")

# Input fields
col1, col2 = st.columns(2)

with col1:
    gdp = st.number_input(
        "GDP per Capita (USD)",
        min_value=0,
        max_value=300000,
        value=10000,
        step=1000,
        help="World Bank data (current US$)"
    )
    rural = st.slider(
        "Rural Population (%)",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=0.5
    )

with col2:
    health = st.number_input(
        "Gov Health Expenditure (% of GDP)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=0.1
    )

st.markdown("---")

# Prediction
if st.button("Predict", type="primary"):
    pred_value = predict_water_access(rural, health, gdp)
    pred_value = max(0, min(100, pred_value))

    status, color = get_status(pred_value)

    # Save to history 
    st.session_state.history.append({
        "GDP": gdp,
        "Rural %": rural,
        "Health %": health,
        "Predicted %": round(pred_value, 1),
        "Status": status
    })

    st.subheader("Prediction Result")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            f"<h1 style='text-align: center; color: {color};'>{pred_value:.1f}%</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='text-align: center; font-size: 1.2em;'>{status}</p>",
            unsafe_allow_html=True
        )

    st.caption(f"GDP: ${gdp:,} | Rural: {rural:.1f}% | Health: {health:.1f}%")

st.markdown("---")

# Display history
if st.session_state.history:
    st.subheader("Prediction History")

    df_history = pd.DataFrame(st.session_state.history)
    st.dataframe(df_history, use_container_width=True)

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()
else:
    st.caption("No predictions yet. Try entering some values above!")