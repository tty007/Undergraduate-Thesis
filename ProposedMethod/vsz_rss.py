# -*- coding: utf-8 -*-
import time
import timeout_decorator
import subprocess
import re
import datetime
import csv
# プロセスチェックコマンド
# while 1; do adb shell ps 21074; done

def load_webpage(url):
    subprocess.call("adb shell am start \
        -n com.android.chrome/com.google.android.apps.chrome.Main \
        -d {}".format(url), shell=True)


@timeout_decorator.timeout(10)
def read_process_figure(name):
    with open('csv_data/rakuten/{}.csv'.format(name), 'w', newline='') as csvfile:
        fieldnames = ['time','USER', 'PID', 'PPID', 'VSZ', 'RSS', 'WCHAN', 'ADDR', 'S', 'NAME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        column = ['USER', 'PID', 'PPID', 'VSZ', 'RSS', 'WCHAN', 'ADDR', 'S', 'NAME']
        i = 0
        for i in range(100):
            privileged_process = subprocess.check_output("adb shell ps | grep com.android.chrome:privileged_process", shell=True).decode('utf-8')
            data = dict(zip(column, privileged_process.split()))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            data.update(time)
            writer.writerow(data)
            i += 1


def run_proposed(num):
    load_webpage('https://rakuten.co.jp')

    try:
        print(str(num) + '回目の実行')
        file_name = 'rakuten_' + str(num)
        read_process_figure(file_name)
    except timeout_decorator.timeout_decorator.TimeoutError:
        if num < 50:
            time.sleep(5)
            print('TimeoutErrror, but retry this code onemore.')
            print(num)
            num += 1
            print(num)
            run_proposed(num)
        else:
            pass

run_proposed(1)