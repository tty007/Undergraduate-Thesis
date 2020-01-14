import csv
import pandas as pd
import glob


def collect_cpu_loads(sitename):

    cols = ['time[ms]']
    df = pd.DataFrame(columns=cols)

    for i in range(9):
        # フォルダ中のパスを取得
        DATA_PATH = "./" + sitename + "/"
        All_Files = glob.glob('{0}cpu_{1}.csv'.format(DATA_PATH, i))

        # フォルダ中の全csvをマージ
        for file in All_Files:
            data = pd.read_csv(file)
            if i == 0:
                df['time[ms]'] = data['time[ms]']
            df['time_{}'.format(i)] = data['time[ms]']
            df['csv_load_{}'.format(i)] = data['cpu_load']
        print(df)
    df.to_csv('{0}/collect_loads.csv'.format(sitename, i), encoding='utf_8')

collect_cpu_loads('amazon')
collect_cpu_loads('google')
collect_cpu_loads('facebook')
collect_cpu_loads('wikipedia')
collect_cpu_loads('netflix')
collect_cpu_loads('linkedin')
collect_cpu_loads('instagram')
collect_cpu_loads('craigslist')
collect_cpu_loads('bing')
collect_cpu_loads('chase')
collect_cpu_loads('paypal')
collect_cpu_loads('apple')
collect_cpu_loads('microsoft')
collect_cpu_loads('stackoverflow')
collect_cpu_loads('wellsfargo')
collect_cpu_loads('worldpress')
collect_cpu_loads('ask')
collect_cpu_loads('fc')
collect_cpu_loads('vimeo')