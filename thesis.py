# -*- coding: utf-8 -*-
import time
import timeout_decorator
from multiprocessing import Pool
import subprocess
import re
import datetime
import csv


def load_webpage(url):
    subprocess.call("adb shell am start \
        -n com.android.chrome/com.google.android.apps.chrome.Main \
        -d {}".format(url), shell=True)


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
@timeout_decorator.timeout(8)
def cpu_info(cpu_id):
    with open("csv_data/cpu_{0}.csv".format(str(cpu_id)), "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'cpu_scaling_freq', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()

        while True:
            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_id_s = str(cpu_id)
            cpu_id = int(cpu_id_s[0])
            cpu_info = cpu_load_related_array[cpu_id].split()[0:8]
            # cpi_idが0でなければ，(1-8であれば)cpu_scaling_freqを取得
            if cpu_id >= 1 and cpu_id <= 8:
                cpu_scaling_freq = get_cpu_scaling_freq(cpu_id)
                # 取得したcpu_scaling_freqをcpu_info(リスト)に結合
                cpu_info.append(cpu_scaling_freq)
            
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'cpu_scaling_freq']
            cpu_info = dict(zip(cpu_index, cpu_info))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_info.update(time)
            writer.writerow(cpu_info)

# オクタコアマルチプロセス用メソッド
def multi_process_cpu(url, load_num_s, load_num):
    # 10スレッドで実行
    thread = Pool(10)
    # ここでページをロード...関数を9回起動するので，cpu_info内に書くとタブが9回開いてしまう
    load_webpage(url)

    # タイムアウトでファイル実行が中止になってしまう為，エラーハンドリングが必要
    cpu_num_list = []
    try:
        for cpu_num in range(9):
            file_num = str(cpu_num) + '_' + str(load_num_s)
            cpu_num_list.append(file_num)
            cpu_num += 1

        thread.map(cpu_info, cpu_num_list)
    except timeout_decorator.timeout_decorator.TimeoutError:
        time.sleep(1)
        if load_num_s <= (load_num-1):
            print('TimeoutErrror, but retry this code onemore.')
            load_num_s += 1
            multi_process_cpu(url=url, load_num_s=load_num_s, load_num=load_num)
        else:
            print('\n\n==========\nThis code finished successfully. Data collected to "csv_data" folder.\n==========\n\n')
            pass


# =========実行==========
# CPU情報取得メソッド
if __name__ == '__main__':
    # 1-5回webページをロードして記録
    multi_process_cpu(url='https://google.co.jp', load_num_s=1, load_num=1)
