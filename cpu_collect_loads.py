import csv
import pandas as pd
import glob


def collect_cpu_loads(sitename):

    cols = ['time[ms]']
    data = pd.DataFrame(columns=cols)

    for load_num in range(1,51):
        for i in range(9):
            # フォルダ中のパスを取得
            DATA_PATH = "./csv_resample_data/" + sitename + "/"
            All_Files = glob.glob('{0}cpu_{1}_{2}.csv'.format(DATA_PATH, i, load_num))

            # フォルダ中の全csvをマージ
            for file in All_Files:
                df = pd.read_csv(file)
                cpu_load = (df['user']+df['system']+df['nice']+df['irq']+df['softirq']+df['steal'])/(df['user']+df['system']+df['nice']+df['iowait']+df['irq']+df['softirq']+df['steal']+df['idle'])
                if i == 0:
                    data['time[ms]'] = df['time[ms]']
                data['cpu_load_{}'.format(i)] = cpu_load

        data.to_csv('final_loads_csv/{0}/collect_loads_{1}.csv'.format(sitename, load_num), encoding='utf_8')

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