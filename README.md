# Umzingwane Hydrological Engine

A hybrid machine learning and physics-informed computational pipeline designed to simulate catchment discharge and assess flood risk for hydraulic structure design.

## 🎯 The Engineering Problem
Standard hydrological analysis often relies on static historical averages which underestimate "Tail Risk" (extreme flood events). This engine provides a stochastic simulation environment to stress-test weir and spillway capacities against climate-adjusted volatility.

## 🏗️ Architecture
The pipeline bridges the gap between high-level data analysis and low-level computational efficiency:

* **The Brain (Python):** Utilizes Scikit-Learn to perform time-series analysis and parameter calibration on historical runoff data.
* **The Brawn (C++):** A Monte Carlo simulation engine (utilizing O3 optimization) capable of generating 150,000+ stochastic realizations for accurate Flow Duration Curve (FDC) development.
* **The Steering Wheel (Streamlit):** An interactive dashboard that allows users to select data scenarios, trigger ML calibration, and visualize discharge risks in real-time.

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* G++ Compiler
* Required libraries: `pip install pandas streamlit`

### Running the Dashboard
1. Navigate to the project directory:
   ```bash
   cd UmzingwaneML