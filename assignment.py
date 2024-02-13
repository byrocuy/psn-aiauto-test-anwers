import pandas as pd
import numpy as np
from datetime import datetime

def count_downtime(df):
    i, total_down = 0, 0
    while i in range(df.shape[0] - 1):
        if df.Value[i] == 1:
            total_down += (df.date_time[i + 1] - df.date_time[i]).seconds
        i += 1

    return total_down

df = pd.read_csv('device_network_data.csv')

df.loc[:, "Value"] = df.Value.replace("Null", np.nan)
df.loc[:, "Value"] = df.Value.ffill()

df["Value"] = df.Value.astype(int)
df["date_time"] = df.loc[:, "Epoch Time"].apply(lambda x: datetime.fromtimestamp(x / 1e3))

downtime = count_downtime(df)
print(f'Total Downtime: {downtime} seconds')