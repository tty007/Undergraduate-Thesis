import csv
import pandas as pd
import glob


def collect_cpu_loads(sitename):

    cols = ['time[ms]']
    data = pd.DataFrame(columns=cols)

    for load_num in range(1,51):

        for i in range(9):
            # フォルダ中のパスを取得
            DATA_PATH = "./final_loads_csv/" + sitename + "/"
            All_Files = glob.glob('{0}collect_loads_{1}.csv'.format(DATA_PATH, load_num))

            # フォルダ中の全csvをマージ
            for file in All_Files:
                df = pd.read_csv(file).fillna(method='bfill')
                p_model = df['cpu_load_0'] * 0.34742197 + df['cpu_load_1'] * -0.18400277 + df['cpu_load_2'] * 0.06652373 + df['cpu_load_3'] * 0.73253027 + df['cpu_load_4'] * 0.55148915 + df['cpu_load_5'] * 0.04289157 + df['cpu_load_6'] * -0.00507745 + df['cpu_load_7'] * -0.26185862 + df['cpu_load_8'] * 0.37044772 - 0.04989937
                data['time[ms]'] = df['time[ms]']
                data['pmodel'] = p_model     

        data.to_csv('final_loads_csv/{0}/p_model_{1}.csv'.format(sitename, load_num), encoding='utf_8')

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
