import numpy as np
import pandas as pd

Individual = pd.read_csv("dataset/RevisedIndividualData.csv")
Individual['age'] = Individual['age'].fillna(0)

Individual['sex'].replace({'female': 0, 'male': 1}, inplace=True)
Individual['country'] = Individual['country'].str.replace(
    'United States', 'US')
# Individual['RecoveryRate'] = Individual['outcome'].replace(
#     {'deceased': 0, 'hospitalized': 0, 'nonhospitalized': 0, 'recovered': 1})
# Individual['Hospitalizations'] = Individual['outcome'].replace(
#     {'deceased': 0, 'hospitalized': 1, 'nonhospitalized': 0, 'recovered': 0})
# Individual['NonHospitalizations'] = Individual['outcome'].replace(
#     {'deceased': 0, 'hospitalized': 0, 'nonhospitalized': 1, 'recovered': 0})
# Individual['deceased'] = Individual['outcome'].replace(
#     {'deceased': 1, 'hospitalized': 0, 'nonhospitalized': 0, 'recovered': 0})

# Grouped_Individual_Age = Individual.groupby(['country', 'province']).agg(
#     {'age': 'mean', 'sex': 'mean', 'RecoveryRate': 'mean', 'Hospitalizations': 'mean', 'NonHospitalizations': 'mean', 'deceased': 'mean'}).reset_index()

# Individual['RecoveryRate'] = Individual['RecoveryRate'].mul(
#     25 / 100)
# Individual['Hospitalizations'] = Individual['Hospitalizations'].mul(
#     .25)
# Individual['NonHospitalizations'] = Individual['NonHospitalizations'].mul(
#     .25)
# Individual['deceased'] = Individual['deceased'].mul(
#     25 / 100)

print(Individual)
Individual.to_csv("MergeData/IndividualData.csv")
