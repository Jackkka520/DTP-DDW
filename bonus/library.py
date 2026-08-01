import numpy as np

# Model parameters (from final polynomial model)
# Order: intercept, rural_pct, gov_health_pct, gdp_per_capita, gdp_per_capita²
BETA = np.array([
    [68.8959],   # intercept
    [-8.4784],   # rural_pct
    [5.1206],    # gov_health_pct
    [3.9875],    # gdp_per_capita
    [-0.0001]    # gdp_per_capita²
])

# Means and stds for normalization (order: rural, health, gdp, gdp²)
MEANS = np.array([37.2889, 11.2968, 23662.74, 1.89e9])
STDS = np.array([21.8730, 5.2541, 36743.05, 8.67e9])


def predict_water_access(rural, health, gdp):
    """
    Predict water access percentage from user inputs.
    
    Args:
        rural: Rural population (%)
        health: Government health expenditure (% of GDP)
        gdp: GDP per capita (USD)
    
    Returns:
        float: Predicted water access percentage (0-100)
    """
    gdp_sq = gdp ** 2
    X_input = np.array([[rural, health, gdp, gdp_sq]])
    X_norm = (X_input - MEANS) / STDS
    X_with_intercept = np.c_[np.ones(X_norm.shape[0]), X_norm]
    pred = X_with_intercept @ BETA
    return float(pred[0][0])


def get_status(pred_value):
    """Get status label and color based on prediction."""
    if pred_value >= 80:
        return "High Access", "green"
    elif pred_value >= 50:
        return "Moderate Access", "orange"
    else:
        return "Low Access", "red"


def get_model_info():
    """Return model performance metrics."""
    return {
        "adjusted_r2": 0.5779,
        "rmse": 19.05,
        "sample_size": 133,
        "features": ["rural_pct", "gov_health_pct", "gdp_per_capita", "gdp_per_capita²"]
    }