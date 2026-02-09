"""
StatsForecast DIY - Configuration Module

Loads environment variables and provides configuration settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path, verbose=False)

# ============================================================================
# Data Paths
# ============================================================================
M5_DATA_PATH = os.getenv("M5_DATA_PATH", "./data/sales_train_validation.csv")
M5_EVAL_PATH = os.getenv("M5_EVAL_PATH", "./data/sales_train_evaluation.csv")
RESULTS_PATH = os.getenv("RESULTS_PATH", "./results")

# Create results directory if it doesn't exist
Path(RESULTS_PATH).mkdir(exist_ok=True)

# ============================================================================
# Model Configuration
# ============================================================================
STATSFORECAST_N_JOBS = int(os.getenv("STATSFORECAST_N_JOBS", "-1"))
STATSFORECAST_VERBOSITY = int(os.getenv("STATSFORECAST_VERBOSITY", "1"))

PYDLM_SOLVER = os.getenv("PYDLM_SOLVER", "powell")

# ============================================================================
# Forecasting Horizons & Splits
# ============================================================================
M5_TRAIN_DAYS = int(os.getenv("M5_TRAIN_DAYS", "1941"))
M5_TEST_HORIZON = int(os.getenv("M5_TEST_HORIZON", "28"))
M5_SEASON_LENGTH = int(os.getenv("M5_SEASON_LENGTH", "7"))

# ============================================================================
# Computation
# ============================================================================
N_JOBS = int(os.getenv("N_JOBS", "-1"))
RANDOM_SEED = int(os.getenv("RANDOM_SEED", "42"))

# ============================================================================
# Logging & Output
# ============================================================================
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
SAVE_INTERMEDIATE = os.getenv("SAVE_INTERMEDIATE", "true").lower() == "true"
PLOT_RESULTS = os.getenv("PLOT_RESULTS", "true").lower() == "true"

# ============================================================================
# PyDLM Models
# ============================================================================
ENABLE_PYDLM = os.getenv("ENABLE_PYDLM", "true").lower() == "true"
PYDLM_TREND_ORDER = int(os.getenv("PYDLM_TREND_ORDER", "1"))
PYDLM_SEASONAL_ORDER = int(os.getenv("PYDLM_SEASONAL_ORDER", "7"))

# ============================================================================
# StatsForecast Models
# ============================================================================
STATSFORECAST_MODELS = [
    m.strip() for m in os.getenv(
        "STATSFORECAST_MODELS",
        "AutoARIMA,AutoTheta,NaiveSeasonality"
    ).split(",")
]

# ============================================================================
# Validation Settings
# ============================================================================
CV_FOLDS = int(os.getenv("CV_FOLDS", "5"))
VAL_SIZE = float(os.getenv("VAL_SIZE", "0.1"))


# ============================================================================
# Helper Functions
# ============================================================================

def get_config_summary() -> dict:
    """Return a dictionary of all configuration values."""
    return {
        "data": {
            "m5_data_path": M5_DATA_PATH,
            "m5_eval_path": M5_EVAL_PATH,
            "results_path": RESULTS_PATH,
        },
        "forecasting": {
            "train_days": M5_TRAIN_DAYS,
            "test_horizon": M5_TEST_HORIZON,
            "season_length": M5_SEASON_LENGTH,
        },
        "models": {
            "statsforecast_models": STATSFORECAST_MODELS,
            "enable_pydlm": ENABLE_PYDLM,
        },
        "computation": {
            "n_jobs": N_JOBS,
            "random_seed": RANDOM_SEED,
        },
    }


def print_config():
    """Pretty print configuration summary."""
    import json
    config = get_config_summary()
    print("\n" + "="*70)
    print("CONFIGURATION SUMMARY")
    print("="*70)
    print(json.dumps(config, indent=2, default=str))
    print("="*70 + "\n")


if __name__ == "__main__":
    print_config()
