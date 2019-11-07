import time
from multiprocessing import Pool
import subprocess
import re
import datetime
import csv


def get_cpu_scaling_freq(cpu_id):
    cpu_id -= 1
    cpu_scaling_freq = str(subprocess.check_output("adb shell cat sys/devices/system/cpu/cpu{}/cpufreq/scaling_cur_freq".format(cpu_id), shell=True).decode('utf-8'))
    print(cpu_scaling_freq.replace('\n',''))
    return cpu_scaling_freq


print(get_cpu_scaling_freq(1))