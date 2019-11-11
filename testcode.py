import pandas as pd
import numpy as np

def resample_csv():
    df = pd.read_csv('csv_data/cpu_0.csv')
    
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S:%f')
    df = df.set_index('time')
    new_df = df.resample('100L').mean()
    diff_df = new_df.diff(axis='index')

    i = 0
    swap_list = []
    while i < len(diff_df):
        new_time = str((np.timedelta64((new_df.index.values[i] - new_df.index.values[0]), 'ms')).astype('uint64'))
        swap_list.append(new_time)
        i += 1

    diff_df.index = swap_list
    diff_df.index.names = ['time[ms]']
    final_df = diff_df
    final_df.to_csv('csv_resample_data/cpu_0.csv')


resample_csv()