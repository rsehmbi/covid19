import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 15)

LocationDataset = pd.read_csv("dataset/CleanedLocations.csv")
Index = pd.read_csv("dataset/OutlierIndex.csv")

IndexList = Index['0'].tolist()
LocationDataset = LocationDataset.drop(LocationDataset.index[IndexList])


# uncomment this line if you require to merge data only for the US as per question 1.4 question

# LocationDataset = LocationDataset[LocationDataset['Country_Region'].str.contains("US")]
Grouped_Location_Data = LocationDataset.groupby(['Country_Region', 'Province_State']).agg(
    {'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Active': 'sum', 'Incidence_Rate': 'mean', 'Case-Fatality_Ratio': 'mean'}).reset_index()
Grouped_Location_Data = Grouped_Location_Data[~Grouped_Location_Data['Province_State'].str.contains(
    "Recovered")]
Grouped_Location_Data.to_csv("MergeData/LocationData.csv")
