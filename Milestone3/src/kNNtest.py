import numpy as np
import pandas as pd
from sklearn.metrics import recall_score, make_scorer, precision_score, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


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


def print_classification_report(n_nneighbors, nmetric, nweights):
    KNN = KNeighborsClassifier(
        n_neighbors=n_nneighbors, weights=nweights, metric=nmetric)

    X_train, y_train = LoadTrainingData()
    KNN.fit(X_train, y_train)

    X_test, y_test = LoadTestData()
    y_pred = KNN.predict(X_test)

    report = classification_report(y_test, y_pred)
    print(report)
    return report


def findNlargestRecall(df):
    df = df.nlargest(5, 'recall_deceased')
    print(df)
    return df


def main():
    ARRD = pd.read_csv("../results/AccuracyRecallRecallDeceasedKNN.csv")
    ndf = findNlargestRecall(ARRD)

    ndf = ndf.apply(lambda x: pd.Series(print_classification_report(
        x.param_n_neighbors, x.param_metric, x.param_weights)), axis=1)

    ndf.to_csv("../results/ClassificationReport_kNN.csv")


if __name__ == "__main__":
    main()
