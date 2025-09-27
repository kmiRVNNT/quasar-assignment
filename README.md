# QUASAR Coding Assignment

This project loads EEG & ECG data from a CSV file and displays them in an interactive Plotly plot.

## Run

From the `src/` folder in `QUASAR`:

```bash
python 1main.py
```

This will:

* Load the dataset (`EEG and ECG data_02_raw.csv`)
* Save an interactive plot as `plot.html`
* Open it automatically in your browser

## Project Structure

* **src/** → final organized scripts (`1main.py`, `plotSIGNLS.py`, `dataLOAD.py`)
* **notebooks/** → personal scratch/testing space (`test.py`) used to prototype before moving code into `src/`

## Notes

* EEG is plotted on the left axis
* ECG is plotted on the right axis
* The plot is zoomable and scrollable
* If given more time, I would add: more EEG channels, filtering, and a nicer GUI
