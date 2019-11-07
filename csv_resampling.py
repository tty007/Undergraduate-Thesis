import pandas as pd

def resample_csv(cpu_id):
    df = pd.read_csv('csv_data/cpu_'+ str(cpu_id) + '.csv')
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S:%f')
    df = df.set_index('time')
    new_df = df.resample('100L').mean()
    new_df.to_csv('csv_resample_data/cpu_' + str(cpu_id) + '.csv')

resample_csv(1)