#  write your code here 
import pandas as pd

data = pd.read_csv('data/dataset/input.txt')

new_data = data.dropna()
print(data.shape[0], new_data.shape[0])
