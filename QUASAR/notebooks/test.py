import pandas as pd

df = pd.read_csv("..\EEG and ECG data_02_raw.csv", comment = "#")
print(df.head())

import plotly.graph_objects as go

fig = go.Figure()

# EEG 
fig.add_trace(go.Scatter(x=df["Time"], y=df["Fz"], name="EEG Fz", yaxis="y1"))

# ECG 
fig.add_trace(go.Scatter(x=df["Time"], y=df["X1:LEOG"], name="ECG LEOG", yaxis="y2"))

# Config axes
fig.update_layout(
    xaxis=dict(title="Time (s)"),
    yaxis=dict(title="EEG (µV)", side="left"),
    yaxis2=dict(title="ECG (mV)", overlaying="y", side="right"),
    title="EEG & ECG Signals",
)
fig.show()
fig.write_html("plot.html")