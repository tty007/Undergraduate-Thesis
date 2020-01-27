import csv
import pandas as pd
import glob


def collect_p_model(sitename):

    cols = ['sitename']
    p_data = pd.DataFrame(columns=cols)

    for load_num in range(1,51):

        # if sitename == 'fc' and load_num == 1:
        #     continue        
        # フォルダ中のパスを取得
        DATA_PATH = "./final_loads_csv/" + sitename + "/"
        All_Files = glob.glob('{0}p_model_{1}.csv'.format(DATA_PATH, load_num))


        # フォルダ中の全csvをマージ
        for file in All_Files:
            data = pd.read_csv(file).drop('Unnamed: 0', axis=1)
            pivot_data = data.pivot_table(columns=['time[ms]'])
            pivot_data['sitename'] = sitename
            p_data = p_data.append(pivot_data)
            # print(p_data)
            # p_data['sitename'] = sitename

    return p_data

amazon = collect_p_model('amazon')
google = collect_p_model('google')
facebook = collect_p_model('facebook')
wikipedia = collect_p_model('wikipedia')
netflix = collect_p_model('netflix')
linkedin = collect_p_model('linkedin')
instagram = collect_p_model('instagram')
craigslist = collect_p_model('craigslist')
bing = collect_p_model('bing')
chase = collect_p_model('chase')
paypal = collect_p_model('paypal')
apple = collect_p_model('apple')
microsoft = collect_p_model('microsoft')
stackoverflow = collect_p_model('stackoverflow')
wellsfargo = collect_p_model('wellsfargo')
worldpress = collect_p_model('worldpress')
ask = collect_p_model('ask')
fc = collect_p_model('fc')
vimeo = collect_p_model('vimeo')


all_data = pd.DataFrame()
all_data = all_data.append([amazon, google, facebook, wikipedia, netflix, linkedin, instagram, craigslist, bing, chase, paypal, apple, microsoft, stackoverflow, wellsfargo, worldpress, ask, fc, vimeo])

all_data.to_csv('final_loads_csv/collect_pmodel.csv')