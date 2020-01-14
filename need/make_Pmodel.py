# -*- coding: utf-8 -*-
import os
import glob
import csv
import pandas as pd

def makePmodel(sitename):

    for i in range(9):
        # フォルダ中のパスを取得
        DATA_PATH = "./" + sitename + "/"
        All_Files = glob.glob('{0}cpu_{1}.csv'.format(DATA_PATH, i))

        # フォルダ中の全csvをマージ
        list = []
        for file in All_Files:
            data = pd.read_csv(file)
            data['sitename'] = sitename
            data['Pmodel'] = -0.00041691 * data['cpu_load'] +  1.07574197
            data = data.drop(['Unnamed: 0', 'cpu_load', 'cpu_scaling_freq'], axis=1)
            list.append(data)
        df = pd.concat(list, sort=False)
        print(df)
        df.to_csv('{0}/p_model_{1}.csv'.format(sitename, i), encoding='utf_8')

makePmodel('amazon')
makePmodel('google')
makePmodel('facebook')
makePmodel('wikipedia')
makePmodel('netflix')
makePmodel('linkedin')
makePmodel('instagram')
makePmodel('craigslist')
makePmodel('bing')
makePmodel('chase')
makePmodel('paypal')
makePmodel('apple')
makePmodel('microsoft')
makePmodel('stackoverflow')
makePmodel('wellsfargo')
makePmodel('worldpress')
makePmodel('ask')
makePmodel('fc')
makePmodel('vimeo')