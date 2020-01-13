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

# CPU_ID/ =0:cpu_all(全体の合計), =1:cpu_1, =2:cpu_2, =3:cpu_3, =4:cpu_4/CPU_load+freq取得関連メソッド
# CPUそれぞれの関数を一つにまとめて簡略化&リサイクル
def power_info(load_num):
    # import pdb; pdb.set_trace()
    with open("only_power_data/vimeo/p_{0}.csv".format(str(load_num)), "w", newline="") as f:
        fieldnames = ['time', 'w']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        # タイムアウト判定用計測変数1
        start = nowtime()
        # シリアルポート接続
        h = serial.Serial("COM5",baudrate=9600,timeout=5)
        while True:
            # タイムアウト判定用計測変数2
            elapsed = math.floor(nowtime() - start)
            
            # 電力取得
            wat = getPowerInfo(h)
            power_info = {'w': wat}
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            power_info.update(time)
            
            writer.writerow(power_info)

            # タイムアウト用例外発生部分
            if elapsed >= 8:
                h.close()
                raise TimeoutError


def process_cpu(url, load_num_s, load_num):
    # ここでページをロード
    load_webpage(url)
    # タイムアウトでファイル実行が中止になってしまう為，エラーハンドリングが必要
    try:
        file_num = str(load_num_s)
        power_info(file_num)
        
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
    process_cpu(url='https://vimeo.com', load_num_s=1, load_num=50)
