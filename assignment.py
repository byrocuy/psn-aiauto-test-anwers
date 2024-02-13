import argparse
import os
import pandas as pd
import numpy as np
from datetime import datetime

def validate_file(file_path):
    if not os.path.exists(file_path):
        raise ValueError(f'File not found: {file_path}')
    return file_path

def count_downtime(df):
    i, total_down = 0, 0
    while i in range(df.shape[0] - 1):
        if df.Value[i] == 1:
            total_down += (df.date_time[i + 1] - df.date_time[i]).seconds
        i += 1

    return total_down

def main(params):
    file_path = params.file_path        

    df = pd.read_csv(file_path)

    df.loc[:, "Value"] = df.Value.replace("Null", np.nan)
    df.loc[:, "Value"] = df.Value.ffill()

    df["Value"] = df.Value.astype(int)
    df["date_time"] = df.loc[:, "Epoch Time"].apply(lambda x: datetime.fromtimestamp(x / 1e3))

    downtime = count_downtime(df)
    print(f'Total Downtime: {downtime} seconds')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate total downtime')

    parser.add_argument('--file_path', default='device_network_data.csv', help='Path to the file', required=True, type=validate_file)
    args = parser.parse_args()
    main(args)