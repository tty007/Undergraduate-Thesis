import time
import subprocess
import re
import datetime
import csv



# CSVの書き込み
with open("csv_data/test.csv", "w", newline="") as f:

    # 要素順を指定します（dictでは順序がわからないため）（フィールドにタイムスタンプも追加）
    fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'time']
    # writerオブジェクトを作成
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
    # writeheaderでヘッダーを出力
    writer.writeheader()

    # 計測時間はここで定義（現在はエンドレスループ）
    while True:
        #まずは情報取ってくる
        cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
        #正規表現でそれぞれのCPU情報をリストに分割
        cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
        #最初の要素，意味不明(b')でなぜか入ってしまうので削除．理由不明
        del cpu_load_related_array[0]

        # とりあえず現時点の出力を記述
        # 798917 19705 376032 239128240 8110 28 11864 0 0 0\n　←CPU全体の指標
        # 196781 5259 132173 59566091 4274 28 8694 0 0 0\n
        # 194283 5059 79582 59861577 1842 0 1070 0 0 0\n
        # 200805 4818 82079 59856965 1083 0 1025 0 0 0\n
        # 207048 4569 82198 59843607 911 0 1075 0 0 0\n'

        # リストの個別要素をさらにリストにする（CPU個別の情報を取り扱う為）
        cpu_all = cpu_load_related_array[0].split()[0:8]
        # 動的に付ける方法もあるが，コア数は端末で事前に調べることができるので静的に変数を設定する．必要な情報のみ格納
        cpu_1 = cpu_load_related_array[1].split()[0:8]
        cpu_2 = cpu_load_related_array[2].split()[0:8]
        cpu_3 = cpu_load_related_array[3].split()[0:8]
        cpu_4 = cpu_load_related_array[4].split()[0:8]
        # オクタコア用
        # cpu_5 = cpu_load_related_array[5].split()[0:8]
        # cpu_6 = cpu_load_related_array[6].split()[0:8]
        # cpu_7 = cpu_load_related_array[7].split()[0:8]
        # cpu_8 = cpu_load_related_array[8].split()[0:8]

        # このコードより後ろで扱いやすいようにデータを辞書型にする
        cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
        cpu_all = dict(zip(cpu_index, cpu_all))
        cpu_1 = dict(zip(cpu_index, cpu_1))
        cpu_2 = dict(zip(cpu_index, cpu_2))
        cpu_3 = dict(zip(cpu_index, cpu_3))
        cpu_4 = dict(zip(cpu_index, cpu_4))

        #時間の計測
        time = datetime.datetime.now().strftime('%H:%M:%S:%f')
        time = dict(time=time)

        #CPU情報にタイムスタンプのキーを追加
        cpu_all.update(time)

        # writerowで1行分を出力
        writer.writerow(cpu_all)