# -*- coding: utf-8 -*-
import os
import glob
import csv
import pandas as pd

def concat(sitename):

    for i in range(9):
        # フォルダ中のパスを取得
        DATA_PATH = "./csv_cpu_load_data/" + sitename + "/"
        All_Files = glob.glob('{0}cpu_{1}_*.csv'.format(DATA_PATH, i))

        # フォルダ中の全csvをマージ
        list = []
        for file in All_Files:
            list.append(pd.read_csv(file))
        df = pd.concat(list, sort=False)
        df.to_csv('need/{0}/cpu_{1}.csv'.format(sitename, i), encoding='utf_8')

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