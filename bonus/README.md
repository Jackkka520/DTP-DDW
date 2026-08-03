# Water Access Predictor

A Streamlit web app that predicts a country's safe drinking water access rate based on economic and demographic indicators.

## Model

- **Algorithm**: Linear Regression with polynomial features (GDP²)
- **Training Data**: World Bank Open Data (2023, 133 countries)
- **Final Features (2 predictors)**:
  - GDP per capita (USD) — log-transformed
  - Rural population (%)

## Performance

| Metric | Value |
|--------|-------|
| Adjusted R² | 0.6768 |
| RMSE | 15.80 percentage points |

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the app:
   streamlit run Home.py

## Deployed Web App

URL: https://dtp-ddw-zc-grp9.streamlit.app/