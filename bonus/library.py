import numpy as np

# ============================================================
# FINAL MODEL: 2 features (Rural + Log_GDP)
# ============================================================
BETA = np.array([
    [68.8243],   # intercept
    [-3.3123],   # rural_pct
    [23.2756]    # log_gdp
])

# Means and stds for normalization (order: rural, log_gdp)
MEANS = np.array([37.2889, 9.1038])
STDS = np.array([21.8730, 1.4859])


def predict_water_access(rural, gdp):
    """
    Predict water access percentage from user inputs.
    Uses final 2-variable model: Rural + Log_GDP.
    """
    gdp = max(gdp, 1)
    log_gdp = np.log(gdp)
    
    X_input = np.array([[rural, log_gdp]])
    X_norm = (X_input - MEANS) / STDS
    X_with_intercept = np.c_[np.ones(X_norm.shape[0]), X_norm]
    pred = X_with_intercept @ BETA
    return float(np.clip(pred[0][0], 0, 100))


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
        "adjusted_r2": 0.6768,
        "rmse": 15.80,
        "sample_size": 133,
        "features": ["rural_pct", "log_gdp"]
    }