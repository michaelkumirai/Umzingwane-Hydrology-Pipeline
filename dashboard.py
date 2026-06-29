import streamlit as st
import subprocess
import pandas as pd
import os

st.set_page_config(page_title="Umzingwane Engine", layout="wide")
st.title("🏗️ Umzingwane Hydrological Steering Wheel")

# 1. Select the file
data_dir = "data"
files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
selected_file = st.selectbox("Select Scenario Data:", files)
file_path = os.path.join(data_dir, selected_file)

num_sims = st.sidebar.number_input("Simulations", value=150000, step=10000)

if st.button("Run Simulation"):
    with st.spinner("Processing..."):
        try:
            # Compile C++ (Only if engine doesn't exist)
            if not os.path.exists("engine/risk_engine.exe"):
                subprocess.run(["g++", "-O3", "engine/main.cpp", "-o", "engine/risk_engine.exe"], check=True)
            
            # Train model using selected file
            subprocess.run(["python", "model/train_stats.py", file_path], check=True)
            
            # Run C++ engine using selected file
            result = subprocess.run(
                ["engine/risk_engine.exe", file_path, "engine/params.txt", str(num_sims)], 
                capture_output=True, text=True, check=True
            )
            
            st.session_state.raw_output = result.stdout
            st.success("Pipeline executed successfully!")
            
        except subprocess.CalledProcessError as e:
            st.error("Pipeline failed!")
            st.code(e.stderr)

# Output parsing
if 'raw_output' in st.session_state:
    output_lines = st.session_state.raw_output.splitlines()
    data_rows = []
    for line in output_lines:
        if "|" in line and "Q" in line:
            parts = line.split("|")
            data_rows.append({"Exceedance": parts[0].strip(), "Flow": float(parts[1].strip())})
            
    df = pd.DataFrame(data_rows)
    st.line_chart(df.set_index("Exceedance"))
    st.table(df)