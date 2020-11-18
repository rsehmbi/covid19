import pandas as pd
import numpy as np
import pickle
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


def LoadTrainingData():
    trainingdata = pd.read_csv("TrainTestData/TrainingData.csv")
    y_train = trainingdata["outcome"].values
    trainingdata = trainingdata[["age", "sex", "latitude", "longitude",
                                 "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_train = trainingdata.values
    return X_train, y_train


def LoadTestData():
    testdata = pd.read_csv("TrainTestData/TestData.csv")
    y_test = testdata["outcome"].values
    testdata = testdata[["age", "sex", "latitude", "longitude",
                         "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_test = testdata.values
    return X_test, y_test


def BuildingkNNModel():
    X_train, y_train = LoadTrainingData()
    neigh = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
    neigh.fit(X_train, y_train)
    dump(neigh, 'kNNwithManhattan.joblib')


def Evaluation():
    kNN = load('kNNwithManhattan.joblib')
    X_train, y_train = LoadTrainingData()
    X_test, y_test = LoadTestData()

    # Metric 1: Validation Scores
    print("Training Score " +
          str(kNN.score(X_train, y_train)))
    print("Validation Score" +
          str(kNN.score(X_test, y_test)))

    # Metric 2: Confusion Matrix
    predicted = kNN.predict(X_test)
    matrix = confusion_matrix(y_test, predicted)
    print("The Confusion Matrix for the prediction is")
    print(matrix)

    # Metric 3: Classification Report
    report = classification_report(y_test, predicted)
    print(report)


def KNN2():
    trainingdata = pd.read_csv("TrainTestData/TrainingData.csv")
    testdata = pd.read_csv("TrainTestData/TestData.csv")

    y_train = trainingdata["outcome"].values
    trainingdata = trainingdata[["age", "sex", "latitude", "longitude",
                                 "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_train = trainingdata.values

    y_test = testdata["outcome"].values
    testdata = testdata[["age", "sex", "latitude", "longitude",
                         "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_test = testdata.values

    neigh = KNeighborsClassifier(n_neighbors=3, metric='minkowski')
    neigh.fit(X_train, y_train)
    print("Score with training " +
          str(neigh.score(X_train, y_train)))
    print("Score with validation " +
          str(neigh.score(X_test, y_test)))


def kNN3():
    trainingdata = pd.read_csv("TrainTestData/TrainingData.csv")
    testdata = pd.read_csv("TrainTestData/TestData.csv")

    y_train = trainingdata["outcome"].values
    trainingdata = trainingdata[["age", "sex", "latitude", "longitude",
                                 "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_train = trainingdata.values

    y_test = testdata["outcome"].values
    testdata = testdata[["age", "sex", "latitude", "longitude",
                         "Confirmed", "Deaths", "Recovered", "Active", "Incidence_Rate", "Case-Fatality_Ratio"]]
    X_test = testdata.values

    neigh = KNeighborsClassifier(n_neighbors=4, metric='euclidean')
    neigh.fit(X_train, y_train)
    print("Score with training " +
          str(neigh.score(X_train, y_train)))
    print("Score with validation " +
          str(neigh.score(X_test, y_test)))


def main():
    BuildingkNNModel()
    Evaluation()
    # KNN2()
    # kNN3()


if __name__ == "__main__":
    main()
