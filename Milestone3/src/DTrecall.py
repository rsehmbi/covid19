import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import recall_score

def LoadTrainingData():
    trainingdata = pd.read_csv("../dataset/TrainingData.csv")
    y_train = trainingdata["outcome"].values
    trainingdata = trainingdata[["age", "sex", "latitude", "longitude",
                                 "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_train = trainingdata.values
    return X_train, y_train

def calculate_recall(nn_estimators, nlearning_rate):
    Model = AdaBoostClassifier(n_estimators = nn_estimators, learning_rate = nlearning_rate)
    X_train, y_train = LoadTrainingData()
    Model.fit(X_train, y_train)
    y_pred = Model.predict(X_train)
    deceased, hospitalized, nonhospitalized, recovered = recall_score(
        y_train, y_pred, average=None, labels=["deceased", "hospitalized", "nonhospitalized", "recovered"])
    return [deceased, hospitalized, nonhospitalized, recovered]

def Recall():
    df = pd.read_csv("../results/TuningDecisionTree.csv")
    df[['recall_deceased', 'recall_hospitalized', 'recall_nonhospitalized', 'recall_recovered']] = df.apply(
        lambda x: pd.Series(calculate_recall(int(x.param_n_estimators), x.param_learning_rate)), axis=1)

    df.to_csv("../results/Recall_DT.csv", index = False)

Recall()
