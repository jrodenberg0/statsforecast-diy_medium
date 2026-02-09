#!/bin/bash

# StatsForecast DIY - Setup Script
# Initializes the project environment and installs dependencies

set -e

echo "=========================================="
echo "StatsForecast DIY - Setup"
echo "=========================================="

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version | awk '{print $2}')
echo "✓ Python $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✓ Pip upgraded"

# Install requirements
echo ""
echo "Installing dependencies..."
echo "  This may take a few minutes..."

# Install with progress
pip install -q -r requirements.txt

echo "✓ Dependencies installed"

# Create necessary directories
echo ""
echo "Creating project directories..."
mkdir -p data results
echo "✓ Directories created"

# Setup .env file
echo ""
echo "Setting up environment file..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✓ .env created from .env.example"
    echo "  ⚠ Update .env with your M5 data path"
else
    echo "✓ .env already exists"
fi

# Install Jupyter kernel for this environment
echo ""
echo "Installing Jupyter kernel..."
pip install -q ipykernel
python3 -m ipykernel install --user --name statsforecast_diy --display-name "StatsForecast DIY" > /dev/null 2>&1
echo "✓ Jupyter kernel installed (statsforecast_diy)"

# Verify installations
echo ""
echo "Verifying installations..."
python3 -c "import statsforecast; print(f'  ✓ StatsForecast {statsforecast.__version__}')" 2>/dev/null || echo "  ⚠ StatsForecast not found"
python3 -c "import pydlm; print(f'  ✓ PyDLM {pydlm.__version__}')" 2>/dev/null || echo "  ⚠ PyDLM not found"
python3 -c "import pandas; print(f'  ✓ Pandas {pandas.__version__}')" 2>/dev/null || echo "  ⚠ Pandas not found"

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Activate environment: source venv/bin/activate"
echo "2. Update .env with your M5 data path"
echo "3. Download M5 data to ./data/"
echo "4. Run: jupyter notebook m5_training.ipynb"
echo ""
