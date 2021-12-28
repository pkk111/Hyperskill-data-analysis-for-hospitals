#  write your code here 
import pandas as pd
data = pd.read_csv('data/dataset/input.txt')

print(data.shape[1] - data.dropna(axis=1).shape[1])
