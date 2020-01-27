import csv
import pandas as pd
import glob
import numpy as np


def collect_cpu_loads(sitename):

    cols = ['sitename']
    data = pd.DataFrame(columns=cols)

    for load_num in range(1,51):
 
        # フォルダ中のパスを取得
        DATA_PATH = "./final_loads_csv/" + sitename + "/"
        All_Files = glob.glob('{0}p_model_{1}.csv'.format(DATA_PATH, load_num))

        # フォルダ中の全csvをマージ
        for file in All_Files:
            df = pd.read_csv(file)
            N = 14 #サンプル数
            # 窓関数
            hw = np.hamming(N) #ハミング窓
            data_head = df['pmodel'].values[1:15]
            windowData = hw * data_head
            # フーリエ変換
            F = np.fft.fft(windowData)
            F_abs = np.abs(F)
            height = F_abs[0:int(N/2)] / np.max(F_abs)

            fft = pd.DataFrame([height], columns=['0', '1', '2', '3', '4', '5', '6'])
            # if sitename == "amazon":
            #     fft['sitename'] = 1
            # elif sitename == "google":
            #     fft['sitename'] = 2
            # elif sitename == "facebook":
            #     fft['sitename'] = 3
            # elif sitename == "wikipedia":
            #     fft['sitename'] = 4
            # elif sitename == "netflix":
            #     fft['sitename'] = 5
            # elif sitename == "linkedin":
            #     fft['sitename'] = 6
            # elif sitename == "instagram":
            #     fft['sitename'] = 7
            # elif sitename == "craigslist":
            #     fft['sitename'] = 8
            # elif sitename == "bing":
            #     fft['sitename'] = 9
            # elif sitename == "chase":
            #     fft['sitename'] = 10
            # elif sitename == "paypal":
            #     fft['sitename'] = 11
            # elif sitename == "apple":
            #     fft['sitename'] = 12
            # elif sitename == "microsoft":
            #     fft['sitename'] = 13
            # elif sitename == "stackoverflow":
            #     fft['sitename'] = 14
            # elif sitename == "wellsfargo":
            #     fft['sitename'] = 15
            # elif sitename == "worldpress":
            #     fft['sitename'] = 16
            # elif sitename == "ask":
            #     fft['sitename'] = 17
            # elif sitename == "fc":
            #     fft['sitename'] = 18
            # elif sitename == "vimeo":
            #     fft['sitename'] = 19

            fft['sitename'] = sitename
            data = data.append(fft)
            # print(height[0])
    # print(data)
    return data
        # data.to_csv('final_loads_csv/{0}/p_model_{1}.csv'.format(sitename, load_num), encoding='utf_8')

amazon = collect_cpu_loads('amazon')
google = collect_cpu_loads('google')
facebook = collect_cpu_loads('facebook')
wikipedia = collect_cpu_loads('wikipedia')
netflix = collect_cpu_loads('netflix')
linkedin = collect_cpu_loads('linkedin')
instagram = collect_cpu_loads('instagram')
craigslist = collect_cpu_loads('craigslist')
bing = collect_cpu_loads('bing')
chase = collect_cpu_loads('chase')
paypal = collect_cpu_loads('paypal')
apple = collect_cpu_loads('apple')
microsoft = collect_cpu_loads('microsoft')
stackoverflow = collect_cpu_loads('stackoverflow')
wellsfargo = collect_cpu_loads('wellsfargo')
worldpress = collect_cpu_loads('worldpress')
ask = collect_cpu_loads('ask')
fc = collect_cpu_loads('fc')
vimeo = collect_cpu_loads('vimeo')
all_data = pd.concat([amazon, google, facebook, wikipedia, netflix, linkedin, instagram, craigslist, bing, chase, paypal, apple, microsoft, stackoverflow, wellsfargo, worldpress, ask, fc, vimeo])


# print(pd.concat(amazon, google))
all_data.to_csv('jurai_fft_data.csv', encoding='utf_8', index=False)
