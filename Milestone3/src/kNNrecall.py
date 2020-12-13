import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import recall_score


def LoadTrainingData():
    trainingdata = pd.read_csv("../dataset/TrainingData.csv")
    y_train = trainingdata["outcome"].values
    trainingdata = trainingdata[["age", "sex", "latitude", "longitude",
                                 "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_train = trainingdata.values
    return X_train, y_train


def calculate_recall(n_nneighbors, nmetric, nweights):
    df = pd.read_csv("../dataset/demo.csv")
    KNN = KNeighborsClassifier(
        n_neighbors=n_nneighbors, weights=nweights, metric=nmetric)

    X_train, y_train = LoadTrainingData()
    KNN.fit(X_train, y_train)

    y_pred = KNN.predict(X_train)
    deceased, hospitalized, nonhospitalized, recovered = recall_score(
        y_train, y_pred, average=None, labels=["deceased", "hospitalized", "nonhospitalized", "recovered"])

    df['recall_deceased'] = deceased
    df['recall_hospitalized'] = hospitalized
    df['recall_nonhospitalized'] = nonhospitalized
    df['recall_recovered'] = recovered

    df.to_csv("../dataset/AccuracyRecallRecallDeceasedKNN.csv")

    return deceased


def Recall():
    df = pd.read_csv("../dataset/TuningkNN.csv")
    df = df.apply(
        lambda x: calculate_recall(x.param_n_neighbors, x.param_metric, x.param_weights), axis=1)


def main():
    Recall()


if __name__ == "__main__":
    main()
