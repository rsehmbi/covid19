import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)


Individual = pd.read_csv("dataset/RevisedIndividualData.csv")
Individual['age'] = Individual['age'].fillna(0)

Individual['sex'].replace({'female': 0, 'male': 1}, inplace=True)
Individual['RecoveryRate'] = Individual['outcome'].replace(
    {'deceased': 0, 'hospitalized': 0, 'nonhospitalized': 0, 'recovered': 1})
Individual['Hospitalizations'] = Individual['outcome'].replace(
    {'deceased': 0, 'hospitalized': 1, 'nonhospitalized': 0, 'recovered': 0})
Individual['NonHospitalizations'] = Individual['outcome'].replace(
    {'deceased': 0, 'hospitalized': 0, 'nonhospitalized': 1, 'recovered': 0})
Individual['deceased'] = Individual['outcome'].replace(
    {'deceased': 1, 'hospitalized': 0, 'nonhospitalized': 0, 'recovered': 0})

Grouped_Individual_Age = Individual.groupby(['country', 'province']).agg(
    {'age': 'mean', 'sex': 'mean', 'RecoveryRate': 'mean', 'Hospitalizations': 'mean', 'NonHospitalizations': 'mean', 'deceased': 'mean'}).reset_index()

Grouped_Individual_Age['RecoveryRate'] = Grouped_Individual_Age['RecoveryRate'].mul(
    25 / 100)
Grouped_Individual_Age['Hospitalizations'] = Grouped_Individual_Age['Hospitalizations'].mul(
    .25)
Grouped_Individual_Age['NonHospitalizations'] = Grouped_Individual_Age['NonHospitalizations'].mul(
    .25)
Grouped_Individual_Age['deceased'] = Grouped_Individual_Age['deceased'].mul(
    25 / 100)

print(Grouped_Individual_Age)
Grouped_Individual_Age.to_csv("MergeData/IndividualData.csv")
