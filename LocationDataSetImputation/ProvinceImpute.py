import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myGeocoder")


def state(coord):
    location = []
    try:
        location = geolocator.reverse(coord)
        address = location.raw['address']
        state = address.get('state', '')
        country = address.get('country', '')
        print(country, state)
        return state
    except:
        return np.nan


ProcessedLocations = pd.read_csv("dataset/processed_location_Sep20th2020.csv")

# If we dont have values in both Latitude and Longitude, and Province State we cannot Impute
ProcessedLocations = ProcessedLocations.dropna(
    how='all', subset=['Lat', 'Province_State'])

print(ProcessedLocations)
# Getting only those files with Na in Province State
Province_State_None = ProcessedLocations[ProcessedLocations['Province_State'].isnull(
)]

Province_State_None.copy()
Province_State_None['geom'] = ProcessedLocations['Long_'].map(
    str) + ', ' + ProcessedLocations['Lat'].map(str)
Province_State_None.copy()

Province_State_None['Province_State'] = Province_State_None.apply(lambda x: state(
    x['geom']), axis=1)

Province_State_None.to_csv('ImputedProvince.csv')
