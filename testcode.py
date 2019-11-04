import datetime

while True:
    time = datetime.datetime.now().strftime('%H:%M:%S:%f')
    datetime = dict(nitiji=time)
    print(datetime)