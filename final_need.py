# -*- coding: utf-8 -*-
import os
import glob
import csv
import pandas as pd

def concat(sitename):

    # フォルダ中のパスを取得
    DATA_PATH = "./need/" + sitename + "/"
    All_Files = glob.glob('{0}all_*.csv'.format(DATA_PATH))

    # フォルダ中の全csvをマージ
    list = []
    for file in All_Files:
        list.append(file)
    return list
    # df = pd.concat(list, sort=False)
    
    # df.to_csv('need/{0}/cpu_{1}.csv'.format(sitename, i), encoding='utf_8')

all_path_list = concat('amazon') + \
                concat('google') + \
                concat('facebook') + \
                concat('wikipedia') + \
                concat('netflix') + \
                concat('linkedin') + \
                concat('instagram') + \
                concat('craigslist') + \
                concat('bing') + \
                concat('chase') + \
                concat('paypal') + \
                concat('apple') + \
                concat('microsoft') + \
                concat('stackoverflow') + \
                concat('wellsfargo') + \
                concat('worldpress') + \
                concat('ask') + \
                concat('fc') + \
                concat('vimeo')

# フォルダ中の全csvをマージ
list = []
for file in all_path_list:
    data = pd.read_csv(file)
    list.append(data)
df = pd.concat(list, sort=False)
df.to_csv('need/all_data.csv', encoding='utf_8', index=False)