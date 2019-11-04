import time
import concurrent.futures
import subprocess
import re
import datetime
import csv


def cpu_all_func():
    with open("csv_data/cpu_all.csv", "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        while True:
            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_all = cpu_load_related_array[0].split()[0:8]
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
            cpu_all = dict(zip(cpu_index, cpu_all))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_all.update(time)
            writer.writerow(cpu_all)


def cpu_1_func():
    with open("csv_data/cpu_1.csv", "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        while True:
            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_1 = cpu_load_related_array[1].split()[0:8]
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
            cpu_1 = dict(zip(cpu_index, cpu_1))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_1.update(time)
            writer.writerow(cpu_1)


def cpu_2_func():
    with open("csv_data/cpu_2.csv", "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        while True:
            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_2 = cpu_load_related_array[2].split()[0:8]
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
            cpu_2 = dict(zip(cpu_index, cpu_2))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_2.update(time)
            writer.writerow(cpu_2)


def cpu_3_func():
    with open("csv_data/cpu_3.csv", "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        while True:
            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_3 = cpu_load_related_array[3].split()[0:8]
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
            cpu_3 = dict(zip(cpu_index, cpu_3))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_3.update(time)
            writer.writerow(cpu_3)


def cpu_4_func():
    with open("csv_data/cpu_4.csv", "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()
        while True:
            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_4 = cpu_load_related_array[4].split()[0:8]
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal']
            cpu_4 = dict(zip(cpu_index, cpu_4))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_4.update(time)
            writer.writerow(cpu_4)


#　プロセスプールを使用する．最初に同時に動かす最大数 max_workers を決めるとプロセスを使いまわしてくれるので上で紹介した普通のスレッドよりかしこい．(Python 3.2以降)
if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    executor.submit(cpu_all_func)
    executor.submit(cpu_1_func)
    executor.submit(cpu_2_func)
    executor.submit(cpu_3_func)
    executor.submit(cpu_4_func)