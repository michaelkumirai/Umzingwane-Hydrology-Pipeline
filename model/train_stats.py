import pandas as pd
import sys
import os

# Get file path from command line arguments
if len(sys.argv) < 2:
    print("Error: No data file provided.")
    sys.exit(1)

data_file = sys.argv[1] # The dashboard will pass this filename

# Load data safely
try:
    df = pd.read_csv(data_file)
    df['Mean'] = df['Flow'].rolling(window=12).mean()
    df['Vol'] = df['Flow'].rolling(window=12).std()
    df.dropna(inplace=True)

    # Write params
    with open('engine/params.txt', 'w') as f:
        f.write(f"{float(df['Mean'].iloc[-1])} {float(df['Vol'].iloc[-1])}")
    print("Training successful.")
except Exception as e:
    print(f"Error during training: {e}")
    sys.exit(1)