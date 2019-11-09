import time
from multiprocessing import Pool
import subprocess
import re
import datetime
import csv


def load_webpage(url):
    subprocess.call("adb shell am start \
        -n com.android.chrome/com.google.android.apps.chrome.Main \
        -d {}".format(url), shell=True)


load_webpage('https://yahoo.co.jp')


# キャッシュを削除すると初回起動画面となりページをロードできない
# subprocess.call("adb shell pm clear com.android.chrome", shell=True)
# adb shell am force-stop com.example.package:com.android.chrome
