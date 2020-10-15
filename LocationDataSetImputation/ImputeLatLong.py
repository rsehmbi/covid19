from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np


def LongLat(cityName):
    # location = geolocator.geocode(coord)
    location = []
    try:
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(cityName)
        lat = location.raw['lat']
        lon = location.raw['lon']
        print("Latitude is ", lat, "Longitude is", lon)
        return pd.Series([lat, lon])
    except:
        return pd.Series([0, 0])


df = pd.read_csv("LatLongMissing.csv")
df[['Lat', 'Long_']] = df.apply(
    lambda row: LongLat(row['Province_State']), axis=1)
df.to_csv("ImputedLongLat.csv")
