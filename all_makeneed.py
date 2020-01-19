# -*- coding: utf-8 -*-
import csv
import pandas as pd

def concat(sitename):
    cpu = pd.read_csv('need/{}/cpu_9.csv'.format(sitename))
    power = pd.read_csv('need/amazon/power.csv', names=('time[ms]', 'w'))
    power['time[ms]'] = power['time[ms]'].astype('int')

    merged = pd.merge(cpu,power, on='time[ms]').drop(["Unnamed: 0"],axis=1)

    merged.to_csv('need/{}/all_9.csv'.format(sitename), index=False)

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