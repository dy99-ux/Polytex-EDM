
import pandas as pd

def load_enterprise_data():
    df = pd.read_csv("enterprise_model_output.csv")
    return df
