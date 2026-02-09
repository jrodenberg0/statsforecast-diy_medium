# StatsForecast DIY - Setup Guide

Complete setup instructions for the M5 forecasting project with StatsForecast, PyDLM, and neural forecasting models.

## Quick Start

### Option 1: Automatic Setup (Recommended)

```bash
cd /Users/jackrodenberg/statsforecast_DIY

# Using bash script
bash setup.sh

# OR using Python script
python3 setup.py
```

### Option 2: Manual Setup

```bash
cd /Users/jackrodenberg/statsforecast_DIY

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create directories
mkdir -p data results

# Copy and configure .env
cp .env.example .env
# Edit .env with your M5 data path
```

## Project Structure

```
statsforecast_DIY/
├── m5_training.ipynb          # Main training notebook
├── config.py                  # Configuration loader
├── requirements.txt           # Python dependencies
├── setup.sh                   # Bash setup script
├── setup.py                   # Python setup script
├── .env                       # Environment variables (created on setup)
├── .env.example              # Environment template
├── README.md                 # Project documentation
├── SETUP.md                  # This file
├── data/                     # M5 dataset (download separately)
│   └── sales_train_validation.csv
└── results/                  # Output directory (auto-created)
    ├── forecasts_vs_actuals.csv
    ├── model_scores.csv
    └── raw_forecasts.csv
```

## Dependencies

### Main Forecasting Libraries
- **statsforecast** (≥1.4.0) - Classical statistical models
- **pydlm** (≥1.1.0) - Dynamic linear models
- **neuralforecast** (≥1.0.0) - Deep learning models
- **nixtla** (≥0.5.0) - Nixtla ecosystem utilities

### Supporting Libraries
- pandas, numpy, polars - Data processing
- torch, pytorch-lightning - Deep learning
- scikit-learn, statsmodels - ML utilities
- python-dotenv - Environment configuration
- jupyter, ipywidgets - Notebook support

See `requirements.txt` for complete list with versions.

## Configuration

All settings are managed via `.env` file.

### Key Configuration Variables

#### Data Paths
```
M5_DATA_PATH=./data/sales_train_validation.csv
M5_EVAL_PATH=./data/sales_train_evaluation.csv
RESULTS_PATH=./results
```

#### Forecasting Settings
```
M5_TRAIN_DAYS=1941          # Days for training
M5_TEST_HORIZON=28          # Forecast horizon
M5_SEASON_LENGTH=7          # Seasonality (weekly)
```

#### Model Configuration
```
STATSFORECAST_MODELS=AutoARIMA,AutoTheta,NaiveSeasonality
ENABLE_PYDLM=true
ENABLE_NEURAL_MODELS=false

PYDLM_TREND_ORDER=1         # 0=level, 1=linear, 2=quadratic
PYDLM_SEASONAL_ORDER=7
PYDLM_SOLVER=powell

NEURALFORECAST_MAX_STEPS=100
NEURALFORECAST_BATCH_SIZE=64
NEURALFORECAST_LEARNING_RATE=0.001
```

#### Computation
```
N_JOBS=-1                   # -1 = use all CPUs
RANDOM_SEED=42
USE_GPU=true
```

#### Logging
```
LOG_LEVEL=INFO
SAVE_INTERMEDIATE=true
PLOT_RESULTS=true
```

## Getting M5 Data

### Download from Kaggle

1. **Create Kaggle account**: https://www.kaggle.com (if you don't have one)

2. **Download M5 files**:
   ```bash
   # Install kaggle CLI (if not already installed)
   pip install kaggle

   # Download M5 competition data
   kaggle competitions download -c m5-forecasting-accuracy

   # Extract to data directory
   unzip m5-forecasting-accuracy.zip -d data/
   ```

3. **Alternative**: Download manually from Kaggle and place CSV files in `./data/`

### Expected Files
- `sales_train_validation.csv` - Training data for model development
- `sales_train_evaluation.csv` - Extended training data for final evaluation
- `sales_test_1.csv` - Test predictions (optional)

## Running the Notebook

### Start Jupyter

```bash
# Activate environment first
source venv/bin/activate

# Launch Jupyter
jupyter notebook m5_training.ipynb
```

### Select the Right Kernel

In Jupyter, go to **Kernel** → **Change kernel** → select **"StatsForecast DIY"**

### Run Cells in Order

The notebook is organized in 10 sections:
1. Setup & Imports
2. Data Functions
3. Load M5 Data
4. Create Train/Test Split
5. Configure Models
6. Train StatsForecast Models
7. Train NeuralForecast Models (optional)
8. Evaluate Performance
9. Results Summary
10. Save Results

## Troubleshooting

### "Module not found" errors
```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade --force-reinstall
```

### GPU not detected
```bash
# Check if torch can see GPU
python3 -c "import torch; print(torch.cuda.is_available())"

# If False, CPU will be used automatically
```

### M5 data path issues
- Check that `M5_DATA_PATH` in `.env` points to correct file
- Verify file exists: `ls -lh ./data/sales_train_validation.csv`

### Slow model training
- Reduce dataset size by filtering stores/items
- Decrease `N_JOBS` if running out of memory
- Enable GPU if available: `USE_GPU=true`

### Memory issues
```bash
# Reduce batch size and parallel jobs
NEURALFORECAST_BATCH_SIZE=32
STATSFORECAST_N_JOBS=2
```

## Loading Configuration in Code

The `config.py` module provides programmatic access to all settings:

```python
from config import (
    M5_DATA_PATH,
    M5_TEST_HORIZON,
    STATSFORECAST_MODELS,
    RANDOM_SEED,
)

# Print summary
from config import print_config
print_config()
```

## PyDLM Examples

```python
from pydlm import dlm, trend, seasonality

# Create model
myDLM = dlm([trend.linearTrend(name='linear_trend'),
             seasonality.seasonalPattern(7, name='weekly')],
            data=time_series_data)

# Fit model
myDLM.fit()

# Forecast
myDLM.predictN(steps=28)
```

## Next Steps

1. ✅ Run setup script
2. 📥 Download M5 data to `./data/`
3. ⚙️ Update `.env` with your settings
4. 🚀 Run `m5_training.ipynb`
5. 📊 Review results in `./results/`

## Support

For issues with:
- **StatsForecast**: https://github.com/Nixtla/statsforecast
- **PyDLM**: https://github.com/wwrechard/pydlm
- **NeuralForecast**: https://github.com/Nixtla/neuralforecast
- **M5 Dataset**: https://www.kaggle.com/competitions/m5-forecasting-accuracy

## Environment Activation

Always activate the virtual environment before working:

```bash
source /Users/jackrodenberg/statsforecast_DIY/venv/bin/activate
```

Or add this alias to your `.bashrc` / `.zshrc`:

```bash
alias statsforecast_diy='source /Users/jackrodenberg/statsforecast_DIY/venv/bin/activate'
```

Then just run: `statsforecast_diy`
