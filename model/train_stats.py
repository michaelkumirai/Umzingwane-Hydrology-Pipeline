import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. Load Data
df = pd.read_csv('../data/Runoff.csv')
# Feature engineering: Use rolling window stats as the "Learning" input
df['Mean'] = df['Flow'].rolling(window=12).mean()
df['Vol'] = df['Flow'].rolling(window=12).std()

# Drop NaNs created by rolling
df.dropna(inplace=True)

# 2. Get the most recent learned parameters
# We use the latest window to calibrate the engine for the "current" river state
params = {
    "mean": float(df['Mean'].iloc[-1]),
    "vol": float(df['Vol'].iloc[-1])
}

# 3. Write to parameters file for C++
with open('../engine/params.txt', 'w') as f:
    f.write(f"{params['mean']} {params['vol']}")

print(f"ML Parameters Learned: Mean={params['mean']}, Vol={params['vol']}")