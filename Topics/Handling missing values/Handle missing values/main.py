#  write your code here 
import pandas as pd

data = pd.read_csv('data/dataset/input.txt')

data.dropna(axis=1, thresh=data.shape[0] - 7, inplace=True)
data.fillna(data.median(), inplace=True)

print(data.head(5))
