import numpy as np
import pandas as pd

A = pd.read_csv("A.csv")
B = pd.read_csv("B.csv")


A = A.rename(columns={'Province_State': 'province',
                      'Country_Region': 'country'})

cols = ['province', 'country']
C = A.merge(B, on=['country', 'province'], how='outer')
D = A.merge(B, on=['country', 'province'], how='inner')
print(C)
print(D.columns)
