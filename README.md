# pythonでadbコマンドを実行. shell=Trueは必要
subprocess.call("adb shell コマンド", shell=True)

# Webページを更新
```
count = 0

while count < 10:
    subprocess.call("adb shell am start \
        -n com.android.chrome/com.google.android.apps.chrome.Main \
        -d http://m.yahoo.co.jp/", shell=True)
        count+=1
```

# CPUloadは以下の式で表される
>cpu_load =(Δuser + Δsystem + Δnice + Δhardirq + Δsof tirq + Δsteal)/(Δuser + Δsystem + Δnice + Δiowait + Δhardirq + Δsoftirq + Δsteal + Δidle)

`cpu  776218 19616 356788 237467803 7935 28 11267 0 0 0`
この情報の場合，左から

* user
* nice
* system
* idle
* iowait (kernel2.5.41から)
* irq (kernel2.6.0-test4から)
* softirq (kernel2.6.0-test4から)
* steal (kernel2.6.11から)
* guest(kernel2.6.24から)
* guest_nice (kernel2.6.33から)

つまり後ろの3つは使わない．サンプリングレートは**10Hz(0.1s)**


# Todo
・proc/statから数値情報を取ってきて，CPU_loadを計算


# 大きな問題点，解決すべき点

1. 一定時間内において細かい時系列データを取るプログラムの書き方
2. CSVファイル形式で書き出す際の文字列スプリットのロジック
3. adbコマンドでCPU情報を参照する前に自動でWebページをリロードするプログラムの書き方の調査
4. CPU周波数と，CPU負荷，同時に取得しながら記録する方法