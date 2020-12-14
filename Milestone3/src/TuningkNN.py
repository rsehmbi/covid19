import numpy as np
import pandas as pd
from sklearn.metrics import recall_score, make_scorer, precision_score, accuracy_score
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
        'n_neighbors': [3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
        'weights': ['distance', 'uniform'],
        'metric': ['manhattan', 'euclidean', 'minkowski']
    }

    scoring = {
        'Accuracy': make_scorer(accuracy_score),
        'recall_score': make_scorer(recall_score, average='macro')
    }

    clf = GridSearchCV(
        Classifier,
        grid_params,
        scoring=scoring,
        refit='Accuracy', return_train_score=True,
        cv=5
    )

    clf.fit(X_train, y_train)
    df = pd.DataFrame(clf.cv_results_)
    print("The best parameter are", clf.best_params_)
    print(df.columns)
    df = df[['param_n_neighbors', 'param_weights', 'param_metric',
             'mean_train_Accuracy', 'mean_train_recall_score']]

    df.to_csv("../results/TuningkNN.csv")

    BestParameters = pd.DataFrame([clf.best_params_])
    BestParameters.to_csv("../results/BestParameters.csv")


def main():
    Tuning()


if __name__ == "__main__":
    main()
