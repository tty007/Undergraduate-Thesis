import pandas as pd
import time

df = pd.read_csv('csv_data/cpu_0.csv')

df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S:%f')

df = df.set_index('time')
ret = df.resample('100L').mean()
print(ret)