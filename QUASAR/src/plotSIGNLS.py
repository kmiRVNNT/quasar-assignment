import plotly.graph_objects as go
import webbrowser
import os

"""Interactive plotly and saves the plot as html, to be popped up in your browser."""

def plot_signals(df, output_file="plot.html"):
    """
    Create an interactive plot for EEG and ECG data.
    Saves as HTML and opens in browser.
    """
    fig = go.Figure()

    # EEG (example: Fz channel)
    fig.add_trace(go.Scatter(
        x=df["Time"], y=df["Fz"],
        name="EEG Fz", yaxis="y1"
    ))

    # ECG (example: X1:LEOG channel)
    fig.add_trace(go.Scatter(
        x=df["Time"], y=df["X1:LEOG"],
        name="ECG LEOG", yaxis="y2"
    ))

    # Layout
    fig.update_layout(
        xaxis=dict(title="Time (s)"),
        yaxis=dict(title="EEG (µV)", side="left"),
        yaxis2=dict(title="ECG (mV)", overlaying="y", side="right"),
        title="EEG & ECG Signals",
    )

    # Save & open
    fig.write_html(output_file)
    webbrowser.open("file://" + os.path.abspath(output_file))
