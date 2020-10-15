from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/processed_location_Sep20th2020.csv",
                 delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['Long_'], df['Lat'])]
gdf = GeoDataFrame(df, geometry=geometry)

# this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)),
         marker='o', color='red', markersize=15)
plt.savefig('Maps/LocationLatitudeLongitude.png')
