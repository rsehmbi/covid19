from countryinfo import CountryInfo
import pandas as pd
import numpy as np


def PopulationCalc(CountryName):
    try:
        country = CountryInfo(CountryName)
        population = country.population()
        return pd.Series([population])
    except:
        return pd.Series([0])


df = pd.read_csv("MissingIncidenceRate.csv")
df[['Population']] = df.apply(
    lambda row: PopulationCalc(row['Country_Region']), axis=1)

df['Incidence_Rate'] = df['Confirmed'] / df['Population'] * 100000
df.to_csv("ImputedIncidenceRate.csv")
