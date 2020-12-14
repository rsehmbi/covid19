import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import recall_score, make_scorer, precision_score, accuracy_score
import matplotlib.pyplot as plt

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

    classifier = RandomForestClassifier(n_jobs = -1)

    grid_params = {
        'n_estimators' : [10, 25, 50, 75, 90, 100],
        'criterion' : ['gini', 'entropy'],
        'max_depth' : [None, 2, 5, 10]
    }

    scoring = {
        'Accuracy': make_scorer(accuracy_score),
        'recall_score': make_scorer(recall_score, average='macro')
    }

    clf = GridSearchCV(
        classifier,
        grid_params,
        scoring = scoring,
        refit = 'Accuracy',
        return_train_score=True,
        n_jobs = -1,
        cv = 5
    )

    clf.fit(X_train, y_train)
    df = pd.DataFrame(clf.cv_results_)
    print("The best parameters are", clf.best_params_)
    print(df.columns)
    df = df[['param_n_estimators', 'param_criterion', 'param_max_depth', 'mean_train_Accuracy', 'mean_train_recall_score']]
    df.to_csv("../results/TuningRandomForest.csv")

    BestParameters = pd.DataFrame([clf.best_params_])
    BestParameters.to_csv("../results/BestParameters_RF.csv")
    

Tuning()