import json
import pandas as pd

with open('records.json') as f:
    data_frame = json.load(f)

data_frame = pd.DataFrame(data_frame)

name = data_frame['name'].value_counts()

hobby = data_frame.loc[data_frame['name']=='jerry','favorite']

hobbies = data_frame.iloc[1:6,1:4:2]

print(hobbies)