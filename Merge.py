import numpy as np
import pandas as pd

IndividualData = pd.read_csv("MergeData/IndividualData.csv")
LocationData = pd.read_csv("MergeData/LocationData.csv")


LocationData = LocationData.rename(columns={'Province_State': 'province',
                                            'Country_Region': 'country'})

cols = ['province', 'country']
OuterJoin = IndividualData.merge(
    LocationData, on=['country', 'province'], how='outer')
InnerJoin = IndividualData.merge(
    LocationData, on=['country', 'province'], how='inner')

InnerJoin.to_csv("MergeData/CombinedData.csv")
print(OuterJoin)
print(InnerJoin)
