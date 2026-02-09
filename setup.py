#!/usr/bin/env python3
"""
StatsForecast DIY Setup Script

Installs dependencies and initializes the project environment.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, description=None):
    """Run a shell command and report status."""
    if description:
        print(f"→ {description}...", end=" ", flush=True)
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        if description:
            print("✓")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if description:
            print("✗")
        print(f"  Error: {e.stderr}", file=sys.stderr)
        raise

def main():
    """Main setup function."""
    print("\n" + "="*50)
    print("StatsForecast DIY - Setup")
    print("="*50 + "\n")

    project_root = Path(__file__).parent

    # Check Python version
    print(f"Python: {sys.version.split()[0]}")
    if sys.version_info < (3, 8):
        print("⚠ Python 3.8+ required", file=sys.stderr)
        sys.exit(1)

    # Create virtual environment
    venv_path = project_root / "venv"
    if not venv_path.exists():
        run_command(f"python3 -m venv {venv_path}", "Creating virtual environment")
    else:
        print("✓ Virtual environment exists")

    # Upgrade pip
    pip_cmd = f"{venv_path}/bin/pip install --upgrade pip setuptools wheel -q"
    run_command(pip_cmd, "Upgrading pip")

    # Install requirements
    req_file = project_root / "requirements.txt"
    pip_install = f"{venv_path}/bin/pip install -r {req_file} -q"
    run_command(pip_install, "Installing dependencies")

    # Create directories
    (project_root / "data").mkdir(exist_ok=True)
    (project_root / "results").mkdir(exist_ok=True)
    print("✓ Directories created")

    # Setup .env
    env_file = project_root / ".env"
    env_example = project_root / ".env.example"
    if not env_file.exists() and env_example.exists():
        import shutil
        shutil.copy(env_example, env_file)
        print("✓ .env created (from .env.example)")
        print("  ⚠ Update .env with your M5 data path")
    else:
        print("✓ .env exists")

    # Install Jupyter kernel
    python_path = venv_path / "bin" / "python"
    kernel_cmd = f"{python_path} -m ipykernel install --user --name statsforecast_diy --display-name 'StatsForecast DIY' -q"
    try:
        run_command(kernel_cmd)
        print("✓ Jupyter kernel installed")
    except:
        print("⚠ Jupyter kernel installation failed (optional)")

    # Verify installations
    print("\nVerifying packages...")
    packages = [
        ("statsforecast", "StatsForecast"),
        ("pydlm", "PyDLM"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
    ]

    for import_name, display_name in packages:
        try:
            module = __import__(import_name)
            version = getattr(module, "__version__", "unknown")
            print(f"  ✓ {display_name} {version}")
        except ImportError:
            print(f"  ⚠ {display_name} - not installed")

    print("\n" + "="*50)
    print("Setup Complete!")
    print("="*50)
    print("\nNext steps:")
    print(f"1. Activate: source {venv_path}/bin/activate")
    print("2. Update .env with your M5 data path")
    print("3. Download M5 data to ./data/")
    print("4. Run: jupyter notebook m5_training.ipynb")
    print()

if __name__ == "__main__":
    main()
