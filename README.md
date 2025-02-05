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
⇨とにかくデータを大量に取ってきて，ダウンサンプリングすればいいのでは？

# 並列/並行処理の実装
~~実装に関しては並行処理を行う．プロセスブールを用いる．最初に同時に動かす最大数 max_workers を決めるとプロセスを使いまわしてくれる(Python 3.2以降)~~

Pythonにはver2.6以降から`multiprocessing`という便利なものがある。これのPoolという機能を用いて並列処理を実装した．以下，公式リファレンスより引用

>> multiprocessing モジュールでは、threading モジュールには似たものが存在しない API も導入されています。その最たるものが Pool オブジェクトです。これは複数の入力データに対して、サブプロセス群に入力データを分配 (データ並列) して関数を並列実行するのに便利な手段を提供します。以下の例では、モジュール内で関数を定義して、子プロセスがそのモジュールを正常にインポートできるようにする一般的な方法を示します。 Pool を用いたデータ並列の基礎的な例は次の通りです:
```
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```

## そもそも並列処理と並行処理の違い
### 並行処理
ある1つの時点では、1つの仕事しかしていないが、複数の仕事間を切り替えることによって、同時にやっているように見えること。
単純に**同時にやること**あるいは**他を待たせないこと**が目的。
### 並列処理
ある1つの時点で、実際に、物理的に、複数の仕事をしていること。使用用途としては**速く**することが目的。

# タイムアウトの実装
自作でデコレーターを作成しようと思ったが，Pythonのライブラリに便利そうなtimeout-decoratorというものがあったのでそれを採用した．
[pnpnpn/timeout-decorator](https://github.com/pnpnpn/timeout-decorator)
## Usage
> 
```
import time
import timeout_decorator

@timeout_decorator.timeout(5)
def mytest():
    print("Start")
    for i in range(1,10):
        time.sleep(1)
        print("{} seconds have passed".format(i))

if __name__ == '__main__':
    mytest()
```

## マシンのスペック
 Hardware Overview:
    - Model Name: iMac
    - Model Identifier: iMac19,2
    - Processor Name: Intel Core i7
    - Processor Speed: 3.2 GHz
    - Number of Processors: 1
    - Total Number of Cores: 6
    - L2 Cache (per Core): 256 KB
    - L3 Cache: 12 MB
    - Hyper-Threading Technology: Enabled
    - Memory: 16 GB
    - Boot ROM Version: 220.260.170.0.0
    - SMC Version (system): 2.47f2
    - Serial Number (system): C02YN0VTJWF1
    - Hardware UUID: F2E1D100-B78B-5D5D-BF56-7463E6DA0546
```
machdep.cpu.core_count: 6
machdep.cpu.thread_count: 12
```
総コア数6, 総スレッド数12が制約条件


# Todo
・proc/statから数値情報を取ってきて，CPU_loadを計算


# 大きな問題点，解決すべき点

~~1. 一定時間内において細かい時系列データを取るプログラムの書き方
  ⇨タイムスタンプと共にデータを取得し，あとでダウンサンプリング~~
  ⇨Clear
~~2. CSVファイル形式で書き出す際の文字列スプリットのロジック
　⇨出力したいデータをリストか辞書型にして，csvライブラリを使ってファイルに出力可能~~
  ⇨Clear
~~3. adbコマンドでCPU情報を参照する前に自動でWebページをリロードするプログラムの書き方の調査~~
  ⇨Clear
~~4. CPU周波数と，CPU負荷，同時に取得しながら記録する方法~~
  ⇨Clear

~~5. CPU_SCALING_FREQENCYの差分を取らずに，そのままデータフレームに結合かつ他のカラムはdiff(差分)を取ったCSVファイルの作成~~
  ⇨Clear
6. 求めた特徴量(リサンプリングデータ)からCPU_LOADを計算し，別ファイルに出力（これがトレーニングデータとなる）

⬇️重回帰

これで従来の手法がほぼ完成

# 提案手法データ集め
`vsz_rss.py`のURL,保存先フォルダ名,ファイル名の名前をサイトごとに変更し，実行
↓
`change_rate_csv.py`のURL,保存先フォルダ名,ファイル名の名前をサイトごとに変更し，実行