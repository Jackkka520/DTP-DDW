# Water Access Predictor

A Streamlit web app that predicts a country's safe drinking water access rate based on economic and demographic indicators.

## Model

- **Algorithm**: Linear Regression with polynomial features (GDP²)
- **Training Data**: World Bank Open Data (2023, 133 countries)
- **Features**:
  - GDP per capita (USD)
  - Rural population (%)
  - Government health expenditure (% of GDP)
  - GDP² (polynomial term)

## Performance

| Metric | Value |
|--------|-------|
| Adjusted R² | 0.5779 |
| RMSE | 19.05 percentage points |

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the app:
   streamlit run Home.py