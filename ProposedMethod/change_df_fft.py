# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


amazon_df = pd.read_csv('change_rate_csv/amazon/amazon_1.csv')
#VSZ
#Amazon

#データフレームを入力したら配列でそのFFTを返します
def return_fft(df):
    N = 64 #サンプル数
    # 窓関数
    hw = np.hamming(N) #ハミング窓
    data = df['RSS'].values[1:65]
    windowData = hw * data
    # フーリエ変換
    F = np.fft.fft(windowData)
    F_abs = np.abs(F)
    return F_abs[0:int(N/2)] / np.max(F_abs)

#cite_nameと番号を入れたらそれに対応するCSVデータを，データフレームとして返します
def read_csv(cite_name, i):
    read_df = pd.read_csv('change_rate_csv/{}/{}_{}.csv'.format(cite_name, cite_name, i))
    return read_df


def change_df_fft(cite_name, correct_n):
    fft_list = []
    cite_name = cite_name
    for i in range(1, 50):
        am = read_csv(cite_name, i)
        am_fft = return_fft(am)
        fft_list.append(am_fft)
        i += 1

    Hz = [i+1 for i in range(32)]
    init_df = pd.DataFrame(fft_list, columns=Hz )
    init_df['page'] = correct_n
    return init_df

    


amazon = change_df_fft('amazon', 1)
apple = change_df_fft('apple', 2)
wikipedia = change_df_fft('wikipedia', 3)

one_df = pd.concat([amazon,apple,wikipedia])
print(one_df.reset_index(drop=True))

one_df.to_csv('fft_csv/all_data_RSS.csv')