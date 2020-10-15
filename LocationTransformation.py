import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)

LocationDataset = pd.read_csv("dataset/processed_location_Sep20th2020.csv")

# LocationDataset = LocationDataset[LocationDataset['Country_Region'].str.contains(
#     "US")]

Grouped_Location_Data = LocationDataset.groupby(['Country_Region', 'Province_State']).agg(
    {'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Active': 'sum', 'Incidence_Rate': 'mean', 'Case-Fatality_Ratio': 'mean'}).reset_index()
Grouped_Location_Data = Grouped_Location_Data[~Grouped_Location_Data['Province_State'].str.contains(
    "Recovered")]
Grouped_Location_Data.to_csv("A.csv")
