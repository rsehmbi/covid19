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

InnerJoin.drop(columns=["Unnamed: 0_x", "Unnamed: 0.1",
                        "Unnamed: 0_y"], inplace=True)
InnerJoin.to_csv("MergeData/CombinedData.csv")
# print(OuterJoin)
print(InnerJoin)
