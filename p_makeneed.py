# -*- coding: utf-8 -*-
import os
import glob
import csv
import pandas as pd

def concat(sitename):

    # フォルダ中のパスを取得
    DATA_PATH = "./csv_power_Data/" + sitename + "/"
    All_Files = glob.glob('{0}p_*.csv'.format(DATA_PATH))

    # フォルダ中の全csvをマージ
    list = []
    for file in All_Files:
        list.append(pd.read_csv(file, names=('time[ms]', 'w')))
    df = pd.concat(list, sort=True, axis=1)
    # print(df['w'].mean(axis='columns'))
    # print(df['time[ms]'].mean(axis='columns'))

    df = pd.concat([df['time[ms]'].mean(axis='columns'), df['w'].mean(axis='columns')], axis=1)
    

    df.to_csv('need/{0}/power.csv'.format(sitename), encoding='utf_8', index=False)

concat('amazon')
concat('google')
concat('facebook')
concat('wikipedia')
concat('netflix')
concat('linkedin')
concat('instagram')
concat('craigslist')
concat('bing')
concat('chase')
concat('paypal')
concat('apple')
concat('microsoft')
concat('stackoverflow')
concat('wellsfargo')
concat('worldpress')
concat('ask')
concat('fc')
concat('vimeo')