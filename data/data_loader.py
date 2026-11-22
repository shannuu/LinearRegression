import pandas as pd

def data_loader(file_name):
    data = pd.read_csv(file_name)
    return data