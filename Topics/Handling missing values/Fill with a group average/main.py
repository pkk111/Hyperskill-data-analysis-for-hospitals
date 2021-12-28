#  write your code here 
import pandas as pd

data = pd.read_csv('data/dataset/input.txt')

data['height'] = data.groupby('location')['height'].apply(lambda x: x.fillna(x.mean().round(1)))
print(data['height'].sum())
