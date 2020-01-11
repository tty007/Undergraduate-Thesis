# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool
import subprocess
import re
import datetime
import csv
import math

import serial
import sys

def getPowerInfo(h):
  h.write(b"\xf0")
  rx = h.read(130)
  v = float(rx[2]<<8|rx[3])/100.0
  i = float(rx[4]<<8|rx[5])/1000.0
  return v * i

def load_webpage(url):
    subprocess.call("adb shell am start \
        -n com.android.chrome/com.google.android.apps.chrome.Main \
        -d {}".format(url), shell=True)

def nowtime():
    start = time.time()
    return start


# cpu_id:1-8/CPU_scaling_freq取得メソッド
# 8コア目のCPUスケーリング周波数を取得
# print(get_cpu_scaling_freq(8))
def get_cpu_scaling_freq(cpu_id):
    cpu_id_s = str(cpu_id)
    cpu_id = int(cpu_id_s[0])
    cpu_id -= 1
    cpu_scaling_freq = str(subprocess.check_output("adb shell cat sys/devices/system/cpu/cpu{}/cpufreq/scaling_cur_freq".format(cpu_id), shell=True).decode('utf-8'))
    return cpu_scaling_freq.replace('\n','')

# CPU_ID/ =0:cpu_all(全体の合計), =1:cpu_1, =2:cpu_2, =3:cpu_3, =4:cpu_4/CPU_load+freq取得関連メソッド
# CPUそれぞれの関数を一つにまとめて簡略化&リサイクル
def cpu_info(cpu_id):
    # import pdb; pdb.set_trace()
    with open("cpu_data/google/cpu_{0}.csv".format(str(cpu_id)), "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'cpu_scaling_freq', 'time', 'w']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        # タイムアウト判定用計測変数1
        start = nowtime()
        h = serial.Serial("COM5",baudrate=9600,timeout=5)
        while True:
            # タイムアウト判定用計測変数2
            elapsed = math.floor(nowtime() - start)

            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            # ここで取り出すCPUを指定
            del cpu_load_related_array[0]
            cpu_id = cpu_id[0]
            # import pdb; pdb.set_trace()
            cpu_info = cpu_load_related_array[int(cpu_id)].split()[0:8]
            

            # cpi_idが0でなければ，(1-8であれば)cpu_scaling_freqを取得
            if int(cpu_id) >= 1 and int(cpu_id) <= 8:
                cpu_scaling_freq = get_cpu_scaling_freq(cpu_id)
                # 取得したcpu_scaling_freqをcpu_info(リスト)に結合
                # 文字列をraw文字列に変換
                cpu_scaling_freq = repr(cpu_scaling_freq)[1:-4]
                cpu_info.append(cpu_scaling_freq)

            # print(cpu_info)
            # ['11307', '3696', '15399', '5489320', '3844', '3350', '2573', '0', '151680']
            
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'cpu_scaling_freq', 'w']
            cpu_info = dict(zip(cpu_index, cpu_info))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_info.update(time)
            # 電力取得
            wat = getPowerInfo(h)
            w = dict(w=wat)
            cpu_info.update(w)
            
            # {'user': '88737', 'nice': '33606', 'system': '158487', 'idle': '39579366', 'iowait': '47113', 'irq': '41731', 'softirq': '34605', 'steal': '0', 'time': '15:56:18:921850'}
            writer.writerow(cpu_info)

            # タイムアウト用例外発生部分
            if elapsed >= 8:
                h.close()
                raise TimeoutError


# オクタコアマルチプロセス用メソッド
def process_cpu(url, load_num_s, load_num):
    # ここでページをロード
    load_webpage(url)
    # タイムアウトでファイル実行が中止になってしまう為，エラーハンドリングが必要
    try:
        file_num = '0_' + str(load_num_s)
        cpu_info(file_num)
        
    except TimeoutError:
        time.sleep(1)
        if load_num_s <= 49:
            print('TimeoutErrror, but retry this code onemore.')
            load_num_s += 1
            process_cpu(url=url, load_num_s=load_num_s, load_num=load_num)
        else:
            print('\n\n==========\nThis code finished successfully. Data collected to "csv_data" folder.\n==========\n\n')
            pass


# =========実行==========
# CPU情報取得メソッド
if __name__ == '__main__':
    # 1-5回webページをロードして記録
    process_cpu(url='https://google.co.jp', load_num_s=1, load_num=50)