from dataLOAD import load_data
from plotSIGNLS import plot_signals

# Adjust path if needed
csv_path = "EEG and ECG data_02_raw.csv"

df = load_data(csv_path)
plot_signals(df)
