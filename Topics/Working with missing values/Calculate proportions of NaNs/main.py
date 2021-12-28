#  write your code here 
import pandas as pd

data = pd.read_csv('data/dataset/input.txt')

print(data.isnull().mean().round(2))
