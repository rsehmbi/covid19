from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import pprint
pd.set_option('display.max_rows', 100)

LocationDataset = pd.read_csv("dataset/processed_location_Sep20th2020.csv")

geolocator = Nominatim(user_agent="myGeocoder")


def city_state_country(coord):
    # location = geolocator.geocode(coord)
    print(coord)
    location = []
    try:
        location = geolocator.reverse(coord)
        address = location.raw['address']
        state = address.get('state', '')
        country = address.get('country', '')
        print(country, state)
        return country, state
    except:
        return "Not Found"

    # if location is None:
    #     print("Hellp")
    # else:
    #     print(location.raw)
    # if not (location.raw['address'] is None):
    #     address = location.raw['address']
    #     city = address.get('city', '')
    #     state = address.get('state', '')
    #     country = address.get('country', '')
    #     print(country)
    # return city, state, country


def extract_state(val):
    word = val.split(',')
    return word[1]


Us = LocationDataset.loc[LocationDataset['Country_Region'] == 'US']
print(Us)

# LocationDataset['geom'] = LocationDataset['Long_'].map(
#     str) + ', ' + LocationDataset['Lat'].map(str)
# LocationDataset = LocationDataset.dropna(subset=['Lat', 'Long_'])

Us = Us.copy()
Us['state'] = Us['Combined_Key'].apply(
    extract_state)

print(Us)
# LocationDataset.to_csv('newdf.csv')

# LocationDataset['Country'] = LocationDataset.apply(lambda x: city_state_country(
#     x['Lat'], x['Long_']), axis=1)

# print(LocationDataset)
# # print(city_state_country("47.470706, -99.704723"))
