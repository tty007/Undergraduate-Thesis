import pandas as pd
import numpy as np

def csv_change_rate(filename):

    df = pd.read_csv('csv_data/wikipedia/{}.csv'.format(filename))
    # 差分の変化率を求める
    new_df = pd.concat([df['time'], df[['VSZ','RSS']].pct_change()], axis=1)
    # print(new_df)
    new_df.set_index('time')

    new_df.to_csv('change_rate_csv/wikipedia/{}.csv'.format(filename))


def run_change_rate():
    i = 1
    while i <= 50:
        filename = 'wikipedia_' + str(i)
        csv_change_rate(filename)
        i += 1

run_change_rate()