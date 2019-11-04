import time
from multiprocessing import Pool
import subprocess
import re
import datetime
import csv

# CPU_ID/ =0:cpu_all(全体の合計), =1:cpu_1, =2:cpu_2, =3:cpu_3, =4:cpu_4
# CPUそれぞれの関数を一つにまとめて簡略化&リサイクル
def cpu_info(cpu_id):
    with open("csv_data/cpu_{0}.csv".format(str(cpu_id)), "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        while True:
            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_info = cpu_load_related_array[cpu_id].split()[0:8]
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
            cpu_info = dict(zip(cpu_index, cpu_info))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_info.update(time)
            writer.writerow(cpu_info)

# マルチプロセス用メソッド
def multi_process_cpu():
    # 6スレッドで実行
    thread = Pool(6)
    # 0-5の範囲でcpu_infoをマルチプロセスで実行
    thread.map(cpu_info, range(5))

multi_process_cpu()