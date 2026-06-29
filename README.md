# Umzingwane Hydrological Engine

## Overview
A hybrid C++ and Python pipeline designed for stochastic hydrological modeling. This project addresses the limitations of static historical averages in civil engineering by utilizing machine learning-driven calibration to identify catchment volatility and assess flood risk.

## Pipeline Architecture
- **Data Layer:** Processes `Runoff.csv` historical time-series data.
- **Learner (Python):** Employs Scikit-Learn to estimate current catchment volatility and mean discharge parameters, replacing fixed-parameter assumptions with data-driven insights.
- **Simulator (C++):** A high-performance Monte Carlo engine that performs 150,000+ realizations to generate Flow Duration Curves (FDC) for structural stress-testing.

## Key Engineering Features
- **Physics-Informed Simulation:** Combines data-driven ML calibration with robust C++ computational efficiency.
- **Risk Mitigation:** Identifies "Tail Risk" flood events that standard static engineering methods often miss.
- **Automated Workflow:** Fully integrated pipeline allowing for rapid re-calibration as new hydrological data is acquired.

## How to Run
1. Ensure Python and a C++ compiler (G++) are installed.
2. Run the training model: `python model/train_stats.py`
3. Compile the simulation engine: `g++ -O3 engine/main.cpp -o risk_engine.exe`
4. Run the simulation: `./risk_engine.exe data/Runoff.csv engine/params.txt 150000`
