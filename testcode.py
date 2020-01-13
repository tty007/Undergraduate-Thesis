import pandas as pd


power_df = pd.read_csv('csv_power_data/amazon/p_1.csv', names=('time[ms]', 'w'))

print(power_df)
 

