# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


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

    

# このようにサイト追記
# amazon = change_df_fft('amazon', 1)
# apple = change_df_fft('apple', 2)
# wikipedia = change_df_fft('wikipedia', 3)
google = change_df_fft('google', 'google')
facebook = change_df_fft('facebook', 'facebook')
amazon = change_df_fft('amazon', 'amazon')
wikipedia = change_df_fft('wikipedia', 'wikipedia')
netflix = change_df_fft('netflix', 'netflix')
linkedin = change_df_fft('linkedin', 'linkedin')
instagram = change_df_fft('instagram', 'instagram')
craigslist = change_df_fft('craigslist', 'craigslist')
bing = change_df_fft('bing', 'bing')
chase = change_df_fft('chase', 'chase')
paypal = change_df_fft('paypal', 'paypal')
apple = change_df_fft('apple', 'apple')
microsoft = change_df_fft('microsoft', 'microsoft')
stackoverflow = change_df_fft('stackoverflow', 'stackoverflow')
wellsfargo = change_df_fft('wellsfargo', 'wellsfargo')
worldpress = change_df_fft('worldpress', 'worldpress')
ask = change_df_fft('ask', 'ask')
fc = change_df_fft('fc', 'fc')
vimeo = change_df_fft('vimeo', 'vimeo')

# このようにデータフレームに結合
# one_df = pd.concat([amazon,apple,wikipedia])
one_df = pd.concat([google,facebook,amazon,wikipedia,netflix,linkedin,instagram,craigslist,bing,chase,paypal,apple,microsoft,stackoverflow,wellsfargo,worldpress,ask,fc,vimeo])

print(one_df.reset_index(drop=True))

one_df.to_csv('fft_csv/19all_data_RSS.csv')