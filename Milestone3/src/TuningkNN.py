import numpy as np
import pandas as pd
from sklearn.metrics import recall_score, make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


def LoadTrainingData():
    trainingdata = pd.read_csv("../dataset/TrainingData.csv")
    y_train = trainingdata["outcome"].values
    trainingdata = trainingdata[["age", "sex", "latitude", "longitude",
                                 "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_train = trainingdata.values
    return X_train, y_train


def LoadTestData():
    testdata = pd.read_csv("../dataset/TestData.csv")
    y_test = testdata["outcome"].values
    testdata = testdata[["age", "sex", "latitude", "longitude",
                         "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_test = testdata.values
    return X_test, y_test


def Tuning():
    X_train, y_train = LoadTrainingData()
    X_test, y_test = LoadTestData()

    Classifier = KNeighborsClassifier(n_jobs=-1)

    grid_params = {
        'n_neighbors': [3],
        'weights': ['distance'],
        'metric': ['manhattan']
    }

    scorers = {
        'recall_score': make_scorer(recall_score)
    }

    refit_score = 'recall_score'

    clf = GridSearchCV(
        Classifier,
        grid_params,
    )

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(recall_score(y_test, y_pred, average=None))


def main():
    Tuning()


if __name__ == "__main__":
    main()
