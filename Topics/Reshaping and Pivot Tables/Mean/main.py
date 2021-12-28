#  write your code here 
import pandas as pd

df = pd.read_csv('data/dataset/input.txt')


print(df.loc[df.labels == 'R', 'null_deg'].mean().round(2))
