import csv
import pandas as pd
import glob


def collect_cpu_loads(sitename):

    cols = ['time[ms]']
    data = pd.DataFrame(columns=cols)

    for load_num in range(1,51):

        if sitename == 'fc' and load_num == 1:
            continue
        p_df = pd.read_csv("csv_power_data/{0}/p_{1}.csv".format(sitename, load_num), header=None)
        # print(p_df[[1]])

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
            
        data['w'] = p_df[[1]]
        data['sitename'] = sitename

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

# amazon = collect_cpu_loads('amazon')
# google = collect_cpu_loads('google')
# facebook = collect_cpu_loads('facebook')
# wikipedia = collect_cpu_loads('wikipedia')
# netflix = collect_cpu_loads('netflix')
# linkedin = collect_cpu_loads('linkedin')
# instagram = collect_cpu_loads('instagram')
# craigslist = collect_cpu_loads('craigslist')
# bing = collect_cpu_loads('bing')
# chase = collect_cpu_loads('chase')
# paypal = collect_cpu_loads('paypal')
# apple = collect_cpu_loads('apple')
# microsoft = collect_cpu_loads('microsoft')
# stackoverflow = collect_cpu_loads('stackoverflow')
# wellsfargo = collect_cpu_loads('wellsfargo')
# worldpress = collect_cpu_loads('worldpress')
# ask = collect_cpu_loads('ask')
# fc = collect_cpu_loads('fc')
# vimeo = collect_cpu_loads('vimeo')
# all_data = pd.concat([amazon, google, facebook, wikipedia, netflix, linkedin, instagram, craigslist, bing, chase, paypal, apple, microsoft, stackoverflow, wellsfargo, worldpress, ask, fc, vimeo])


# # print(pd.concat(amazon, google))
# all_data.to_csv('final_loads_csv/all_loads.csv', encoding='utf_8')
