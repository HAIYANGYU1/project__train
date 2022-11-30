
import pandas as pd

data = pd.read_csv('radar.csv',sep=';')
d = data.d.tolist()

num = 0
count = 1
for n in d:
    if n < 1000:
        num = num + count
        count = 0
    else:
        count = 1
    print(f'"num:"{num},"count:"{count}')
        