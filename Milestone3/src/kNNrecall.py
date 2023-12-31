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
    KNN = KNeighborsClassifier(
        n_neighbors=n_nneighbors, weights=nweights, metric=nmetric)

    X_train, y_train = LoadTrainingData()
    KNN.fit(X_train, y_train)

    y_pred = KNN.predict(X_train)
    deceased, hospitalized, nonhospitalized, recovered = recall_score(
        y_train, y_pred, average=None, labels=["deceased", "hospitalized", "nonhospitalized", "recovered"])

    return [deceased, hospitalized, nonhospitalized, recovered]


def Recall():
    df = pd.read_csv("../results/TuningkNN.csv")
    df[['recall_deceased', 'recall_hospitalized', 'recall_nonhospitalized', 'recall_recovered']] = df.apply(
        lambda x: pd.Series(calculate_recall(x.param_n_neighbors, x.param_metric, x.param_weights)), axis=1)

    df.to_csv("../results/AccuracyRecallRecallDeceasedKNN.csv")


def main():
    Recall()


if __name__ == "__main__":
    main()
