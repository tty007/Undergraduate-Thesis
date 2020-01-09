import subprocess
import re
import datetime
import csv
from threading import Thread
import functools

def timeout(seconds_before_timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('関数[%s]は設定時間により終了 [%s seconds] 超過!' % (func.__name__, seconds_before_timeout))]
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(seconds_before_timeout)
            except Exception as e:
                print('error starting thread')
                raise e

            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

@timeout(3)
def test():
    with open("test.csv".format(str(1)), "w", newline="") as f:
        fieldnames = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'cpu_scaling_freq', 'time']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"', lineterminator='\n')
        writer.writeheader()

        while True:

            cpu_load_related = str(subprocess.check_output("adb shell cat proc/stat | grep cpu", shell=True))
            cpu_load_related_array = re.split('cpu[0-9]*\s+', cpu_load_related)
            del cpu_load_related_array[0]
            cpu_info = cpu_load_related_array[1].split()[0:8]

            print(cpu_info)
            cpu_index = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'cpu_scaling_freq']
            cpu_info = dict(zip(cpu_index, cpu_info))
            time = datetime.datetime.now().strftime('%H:%M:%S:%f')
            time = dict(time=time)
            cpu_info.update(time)

            writer.writerow(cpu_info)
            print(cpu_info)

test()