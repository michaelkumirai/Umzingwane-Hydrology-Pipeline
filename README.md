
# Umzingwane Hydrological Engine

## Overview
A hybrid C++ and Python pipeline designed for stochastic hydrological modeling. This project addresses the limitations of static historical averages in civil engineering by utilizing machine learning-driven calibration to identify catchment volatility and assess flood risk.

## Pipeline Architecture
- **Data Layer:** Processes historical time-series data from the `/data` directory.
- **Learner (Python):** Employs Scikit-Learn to estimate current catchment volatility and mean discharge parameters, replacing fixed-parameter assumptions with data-driven insights.
- **Simulator (C++):** A high-performance Monte Carlo engine that performs 150,000+ realizations to generate Flow Duration Curves (FDC) for structural stress-testing.
- **Steering Wheel (Dashboard):** An interactive Streamlit interface that automates compilation, execution, and visualization.

## Key Engineering Features
- **Physics-Informed Simulation:** Combines data-driven ML calibration with robust C++ computational efficiency.
- **Risk Mitigation:** Identifies "Tail Risk" flood events that standard static engineering methods often miss.
- **Automated Workflow:** Fully integrated pipeline allowing for rapid re-calibration as new hydrological data is acquired.

## How to Run
The pipeline is operated via the interactive Streamlit dashboard, which automates the build and execution process.

1. Ensure Python, a C++ compiler (G++), and the required libraries are installed:
```bash
pip install pandas streamlit
```
2. Navigate to the project directory:
```bash
cd UmzingwaneML
```
3. Launch the dashboard:
```bash
streamlit run dashboard.py
```
4. Use the sidebar to select your data scenario and click **"Run Simulation"**. The dashboard will automatically handle the compilation of the C++ engine, the training of the ML model, and the generation of your Flow Duration Curve.
