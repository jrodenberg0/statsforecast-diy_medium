# StatsForecast DIY - M5 Forecasting

Build and test forecasting models on the M5 dataset using StatsForecast and NeuralForecast.

## Structure

```
statsforecast_DIY/
├── m5_training.ipynb           # Main M5 training notebook
├── README.md                    # This file
├── requirements.txt             # Dependencies
├── .gitignore                   # Git ignores
├── data/                        # M5 data (optional local copy)
│   └── sales_train_validation.csv
└── results/                     # Output directory (auto-created)
    ├── forecasts_vs_actuals.csv
    ├── model_scores.csv
    └── raw_forecasts.csv
```

## Quick Start

1. **Prepare M5 data**: Download from [Kaggle M5 Forecasting](https://www.kaggle.com/competitions/m5-forecasting-accuracy) and place in `./data/`
2. **Update data path** in cell 3 if needed
3. **Select models** in cell 5 (StatsForecast and/or NeuralForecast)
4. **Run the notebook** to train and evaluate

## Notebook Sections

1. **Setup & Imports** - Required libraries
2. **Data Functions** - M5 data transformation and metric functions
3. **Load M5 Data** - Load sales data and preprocessing
4. **Create Train/Test Split** - Standard M5 split (1941 days train, 28 days test)
5. **Configure Models** - Define StatsForecast and NeuralForecast models
6. **Train StatsForecast Models** - Classical statistical models (ARIMA, Theta, etc.)
7. **Train NeuralForecast Models** - Deep learning models (optional, currently disabled)
8. **Evaluate Performance** - Compute RMSE and MAPE scores
9. **Results Summary** - Display model rankings
10. **Save Results** - Export forecasts and scores to CSV

## M5 Dataset

- **Time series**: ~30,000 product-store combinations
- **Frequency**: Daily sales data
- **Horizon**: 28-day forecasts
- **Train period**: 1,941 days (Jan 2011 - Dec 2015)
- **Test period**: 28 days (Jan 2016)

## Models

### StatsForecast (Classical)
- AutoARIMA - Automatic ARIMA selection
- AutoTheta - Automatic Theta selection
- NaiveSeasonality - Seasonal naive baseline

### NeuralForecast (Deep Learning, Optional)
- DLinear - Deep linear model with trainable basis functions

## Metrics

- **RMSE** - Root Mean Squared Error (scale-dependent)
- **MAPE** - Mean Absolute Percentage Error (scale-free)

## Output Files

- `forecasts_vs_actuals.csv` - Full test set with predictions and actual values
- `model_scores.csv` - RMSE and MAPE scores by model
- `raw_forecasts.csv` - Raw forecast dataframe
