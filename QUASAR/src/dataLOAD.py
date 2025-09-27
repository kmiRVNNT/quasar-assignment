import pandas as pd

"""This will be where I'll LOAD the csv, skipping all the metadata lines."""

def load_data(path: str):   
    return pd.read_csv(path, comment="#")
