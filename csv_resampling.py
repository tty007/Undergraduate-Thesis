import pandas as pd
import numpy as np

def resample_csv(cpu_id):
    df = pd.read_csv('csv_data/cpu_' + str(cpu_id) + '.csv')
    
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S:%f')
    df = df.set_index('time')
    new_df = df.resample('100L').mean()
    diff_df = new_df.diff(axis='index')

    row_num = 0
    swap_list = []
    while row_num < len(diff_df):
        new_time = str((np.timedelta64((new_df.index.values[row_num] - new_df.index.values[0]), 'ms')).astype('uint64'))
        swap_list.append(new_time)
        row_num += 1

    diff_df.index = swap_list
    diff_df.index.names = ['time[ms]']
    final_df = diff_df
    final_df.to_csv('csv_resample_data/cpu_' + str(cpu_id) + '.csv')

# resample_csv(1)
# resample_csv(2)
# resample_csv(3)
# resample_csv(4)

def file_name(load_num):
    cpu_id = 0
    load_num_s = 1
    file_id = []
    while load_num_s <= load_num:
        while cpu_id <= 8:
            filename = str(cpu_id) + '_' + str(load_num_s)
            file_id.append(filename)
            cpu_id += 1
        load_num_s += 1
        cpu_id = 0
    return file_id


def run_resampling():
    # load_numを手動で指定
    file_id_list = file_name(load_num=5)
    for index, item in enumerate(file_id_list):
        resample_csv(file_id_list[index])
    

run_resampling()