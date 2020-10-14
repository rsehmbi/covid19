import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)


Individual = pd.read_csv("dataset/processed_individual_cases_Sep20th2020.csv")
Individual['age'] = Individual['age'].fillna(0)
Grouped_Individual_Age = Individual.groupby(['country', 'province']).agg(
    {'age': 'mean'}).reset_index()


# Grouped_Individual_Age = Grouped_Individual_Age[~Grouped_Individual_Age['Province_State'].str.contains(
#     "Recovered")]
print(Grouped_Individual_Age)
