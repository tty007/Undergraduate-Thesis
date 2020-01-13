import pandas as pd
import numpy as np

def cal_cpu_load(cpu_id):
    df = pd.read_csv('csv_resample_data/vimeo/cpu_' + str(cpu_id) + '.csv')
    # CPU_loadの計算
    cpu_load = (df['user']+df['system']+df['nice']+df['irq']+df['softirq']+df['steal'])/(df['user']+df['system']+df['nice']+df['iowait']+df['irq']+df['softirq']+df['steal']+df['idle'])
    cpu_load_df = pd.DataFrame({'cpu_load': cpu_load})
    print(cpu_load)
    
    # column_df = pd.concat([cpu_load_df, df.drop(['user', 'system', 'nice', 'idle', 'iowait', 'irq', 'softirq', 'steal'], axis=1)])
    add_df = pd.concat([cpu_load_df, df], axis=1)
    column_df = add_df.drop(['user', 'system', 'nice', 'idle', 'iowait', 'irq', 'softirq', 'steal'], axis=1)
    time_df = column_df.set_index('time[ms]')
    time_df.to_csv('csv_cpu_load_data/vimeo/cpu_' + str(cpu_id) + '.csv')


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


def run_cal():
    # load_num(ページ更新回数：データの回数分の個数)を手動で指定
    file_id_list = file_name(load_num=50)
    for index, item in enumerate(file_id_list):
        cal_cpu_load(file_id_list[index])
    

run_cal()
