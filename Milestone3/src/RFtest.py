import numpy as np
import pandas as pd
from sklearn.metrics import recall_score, make_scorer, precision_score, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
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

def print_classification_report(nn_estimators, ncriterion, nmax_depth):
    RF = RandomForestClassifier(n_estimators = nn_estimators, criterion = ncriterion, max_depth = nmax_depth)
    X_train, y_train = LoadTrainingData()
    RF.fit(X_train, y_train)
    X_test, y_test = LoadTestData()
    y_pred = RF.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)
    return report

def findNlargestRecall(df):
    df = df.nlargest(5, 'recall_deceased')
    print(df)
    return df

def main():
    d = pd.read_csv("../results/Recall_RF.csv")
    ndf = findNlargestRecall(d)
    ndf = ndf.apply(lambda x: pd.Series(print_classification_report(x.param_n_estimators, x.param_criterion, x.param_max_depth)), axis=1)
    ndf.to_csv("../results/ClassificationReport_RF.csv")

main()


