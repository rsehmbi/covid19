import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score

def LoadTrainingData():
    trainingdata = pd.read_csv("../dataset/TrainingData.csv")
    y_train = trainingdata["outcome"].values
    trainingdata = trainingdata[["age", "sex", "latitude", "longitude",
                                 "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_train = trainingdata.values
    return X_train, y_train

def calculate_recall(nn_estimators, ncriterion, nmax_depth):
    RF = RandomForestClassifier(n_estimators = nn_estimators, criterion = ncriterion, max_depth = nmax_depth)
    X_train, y_train = LoadTrainingData()
    RF.fit(X_train, y_train)
    y_pred = RF.predict(X_train)
    deceased, hospitalized, nonhospitalized, recovered = recall_score(
        y_train, y_pred, average=None, labels=["deceased", "hospitalized", "nonhospitalized", "recovered"])
    return [deceased, hospitalized, nonhospitalized, recovered]

def Recall():
    df = pd.read_csv("../results/TuningRandomForest.csv")
    df[['recall_deceased', 'recall_hospitalized', 'recall_nonhospitalized', 'recall_recovered']] = df.apply(
        lambda x: pd.Series(calculate_recall(x.param_n_estimators, x.param_criterion, x.param_max_depth)), axis=1)

    df.to_csv("../results/Recall_RF.csv")


Recall()
