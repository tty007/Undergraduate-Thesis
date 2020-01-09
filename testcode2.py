import time
import math


def spend_time():
    start = time.time()
    while True:
        elapsed = math.floor(time.time() - start)
        print(type(elapsed))


spend_time()
