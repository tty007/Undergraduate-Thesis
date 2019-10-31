# import sys
import time
import subprocess
import re

# pythonでadbコマンドを実行. shell=Trueは必要＝＝＝＝＝
# subprocess.call("adb shell コマンド", shell=True)
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝


# Webページを更新＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# count = 0

# while count < 10:
#     subprocess.call("adb shell am start \
#         -n com.android.chrome/com.google.android.apps.chrome.Main \
#         -d http://m.yahoo.co.jp/", shell=True)
#     count+=1
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝


# CPUloadは以下の式で表されるーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#     =(Δuser + Δsystem + Δnice + Δhardirq + Δsof tirq + Δsteal)/
#     (Δuser + Δsystem + Δnice + Δiowait + Δhardirq + Δsoftirq + Δsteal + Δidle)

# cpu  776218 19616 356788 237467803 7935 28 11267 0 0 0
# この情報の場合，左から
# user nice system idle iowait (kernel2.5.41から) 
# irq (kernel2.6.0-test4から) softirq (kernel2.6.0-test4から) steal (kernel2.6.11から) guest (kernel2.6.24から) guest_nice (kernel2.6.33から)
# つまり後ろの3つは使わない．サンプリングレートは10Hz(0.1s)
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

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
all_cpu = cpu_load_related_array[0].split()[0:8]
# 動的に付ける方法もあるが，コア数は端末で事前に調べることができるので静的に変数を設定する．必要な情報のみ格納
cpu_1 = cpu_load_related_array[1].split()[0:8]
cpu_2 = cpu_load_related_array[2].split()[0:8]
cpu_3 = cpu_load_related_array[3].split()[0:8]
cpu_4 = cpu_load_related_array[4].split()[0:8]
# cpu_5 = cpu_load_related_array[5].split()[0:8]
# cpu_6 = cpu_load_related_array[6].split()[0:8]
# cpu_7 = cpu_load_related_array[7].split()[0:8]
# cpu_8 = cpu_load_related_array[8].split()[0:8]

# このコードより後ろで扱いやすいようにデータを辞書型にする
cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
cpu_1 = dict(zip(cpu_index, cpu_1))
cpu_2 = dict(zip(cpu_index, cpu_2))
cpu_3 = dict(zip(cpu_index, cpu_3))
cpu_4 = dict(zip(cpu_index, cpu_4))








# Todo
# ・proc/statから数値情報を取ってきて，CPU_loadを計算


# 大きな問題点，解決すべき点==============================================================

# 1. 一定時間内において細かい時系列データを取るプログラムの書き方
# 2.　CSVファイル形式で書き出す際の文字列スプリットのロジック
# 4.　adbコマンドでCPU情報を参照する前に自動でWebページをリロードするプログラムの書き方の調査
# 3.　CPU周波数と，CPU負荷，同時に取得しながら記録する方法