#  write your code here 
import pandas as pd

data = pd.read_csv('data/dataset/input.txt')

data['totsp'].fillna(data['livingsp'] + data['nonlivingsp'], inplace=True)

print(int(data['totsp'].agg(sum)))
