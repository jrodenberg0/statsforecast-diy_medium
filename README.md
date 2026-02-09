# M5 Forecasting - DIY StatsForecast

Training and evaluating forecasting models on the M5 dataset using StatsForecast with time series decomposition approaches via PyDLM.

## Overview

This project implements and compares classical statistical forecasting models on the M5 Kaggle competition dataset. It demonstrates various approaches to weekly sales forecasting, including:
- Seasonal naive baselines
- Exponential smoothing
- Dynamic Linear Models (PyDLM) with different components (level, trend, seasonal)

## Quick Start

### Setup
```bash
# Install dependencies
pip install -r requirements.txt
# or with poetry
poetry install

# Create data directory
mkdir -p data
```

### Run the Notebook
```bash
jupyter notebook m5_training.ipynb
```

The notebook will automatically:
1. Download M5 dataset from `datasetsforecast.m5`
2. Aggregate daily sales to weekly frequency (W-SAT)
3. Train models using cross-validation (4 windows, 13-step horizon)
4. Evaluate and visualize performance

## Notebook Sections

1. **Setup & Imports** - Required libraries and directory setup
2. **Load M5 Data** - Fetch M5 dataset and aggregate to weekly
3. **Configure Models** - Define 7 competing models
4. **Train StatsForecast Models** - Cross-validation training on 500 time series
5. **Evaluate Performance** - MAE, bias, and relative MAE metrics
6. **Performance Visualization** - Plot model performance over time

## Dataset

- **Source**: M5 Kaggle Competition (via datasetsforecast)
- **Time series**: 30,000+ product-store combinations
- **Frequency**: Daily sales (aggregated to **weekly** in this project)
- **Train period**: Full historical data available
- **Evaluation**: 4-window cross-validation with 13-week forecast horizon

## Models Implemented

| Model | Type | Description |
|-------|------|-------------|
| **SeasonalNaive** | Baseline | Uses sales from 52 weeks prior (seasonal period) |
| **SESOpt** | Exponential Smoothing | Simple Exponential Smoothing - Optimized |
| **SeasonalNaiveWDrift** | Baseline | Seasonal Naive with drift component |
| **LocalLevel** | PyDLM | Local level model (degree=0, discount=0.8) |
| **LevelTrend** | PyDLM | Level + trend components (degree=1, discount=0.98) |
| **LevelMonthlySeasonal** | PyDLM | Level + monthly seasonality (discount=0.995) |
| **LevelTrendSeasonal** | PyDLM | Level + trend + 52-week seasonality (discount=0.995) |

## Evaluation Metrics

- **MAE** - Mean Absolute Error (units of sales)
- **Bias** - Average directional error (over/under forecasting)
- **RMAE** - Relative MAE vs SESOpt baseline (benchmark: 90% of M5 contestants couldn't beat this)

## Key Findings

- SESOpt consistently performs well as a baseline
- Dynamic Linear Models with appropriate components competitive
- Weekly aggregation reduces data sparsity vs daily forecasting

## Output

Results are generated during notebook execution:
- Cross-validation forecasts with actual vs predicted values
- Performance metrics by model and cutoff period
- Visualizations of MAE + Bias over time

## Project Structure

```
statsforecast-diy_medium/
├── m5_training.ipynb              # Main notebook (source of truth)
├── README.md                       # This file
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Poetry configuration
├── models.py                       # Custom model implementations
├── config.py                       # Configuration settings
├── setup.py                        # Package setup
├── setup.sh                        # Shell setup script
├── .env.example                    # Environment template
├── data/                           # M5 data (auto-downloaded)
└── results/                        # Output directory (auto-created)
```

## Requirements

See `requirements.txt` or `pyproject.toml`. Key dependencies:
- statsforecast
- datasetsforecast
- pandas, numpy
- PyDLM (for dynamic linear models)
- matplotlib (visualization)

## License

Open for educational and research purposes.
