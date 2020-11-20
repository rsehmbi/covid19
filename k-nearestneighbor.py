import pandas as pd
import numpy as np
import pickle
from joblib import dump, load
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import learning_curve
from sklearn.metrics import classification_report
import seaborn as sns


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
    neigh = KNeighborsClassifier(n_neighbors=3, metric='minkowski')
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
    labels = ['True deceased', 'Negative', 'Negative', 'Negative', 'Negative', 'True hospitalized',
              'Negative', 'Negative', 'Negative', 'Negative', ' True nonhospitalized', 'Negative', 'Negative', 'Negative', 'Negative', 'True recovered']
    labels = np.asarray(labels).reshape(4, 4)
    matrix = confusion_matrix(y_test, predicted)

    print("The Confusion Matrix for the prediction is")
    print(matrix)
    fig = sns.heatmap(matrix, annot=labels, fmt='', cmap='Blues', cbar=False)
    plt.xlabel("True classes")
    plt.ylabel("Predicted Classes")
    fig.figure.savefig("kNNConfusionMatrix.png")

    # Metric 3: Classification Report
    report = classification_report(y_test, predicted)
    print(report)


def Overfitting():
    kValues = [i for i in range(1, 50, 2)]

    print(kValues)
    Accuracy = []

    X_train, y_train = LoadTrainingData()

    for k in kValues:
        knn = KNeighborsClassifier(n_neighbors=k, metric='minkowski')
        CrossValidationScore = cross_val_score(
            knn, X_train, y_train, cv=5, n_jobs=-1, scoring='accuracy')
        Accuracy.append(CrossValidationScore.mean())

    kOptimal = kValues[Accuracy.index(max(Accuracy))]
    print(Accuracy)
    print("Optimal k", kOptimal)
    plt.clf()
    plt.plot(kValues, Accuracy)
    plt.xlabel("K Values")
    plt.ylabel(" Accuracy")
    plt.savefig('kValuesVSAccuracy.png')


def LearningCurve():
    X, y = LoadTrainingData()
    train_sizes, train_scores, test_scores = learning_curve(KNeighborsClassifier(),
                                                            X,
                                                            y,
                                                            # Number of folds in cross-validation
                                                            cv=10,
                                                            # Evaluation metric
                                                            scoring='accuracy',
                                                            # Use all computer cores
                                                            n_jobs=-1,
                                                            # 20 different sizes of the training set
                                                            train_sizes=np.linspace(0.01, 1.0, 50))

    # Create means and standard deviations of training set scores
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)

    # Create means and standard deviations of test set scores
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    # Draw lines
    plt.plot(train_sizes, train_mean, '--',
             color="#111111",  label="Training score")
    plt.plot(train_sizes, test_mean, color="#111111",
             label="Cross-validation score")

    # Draw bands
    plt.fill_between(train_sizes, train_mean - train_std,
                     train_mean + train_std, color="#DDDDDD")
    plt.fill_between(train_sizes, test_mean - test_std,
                     test_mean + test_std, color="#DDDDDD")

    # Create plot
    plt.title("Learning Curve")
    plt.xlabel("Training Set Size"), plt.ylabel(
        "Accuracy Score"), plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig('kNNLearningCurve.png')


def main():
    BuildingkNNModel()
    Evaluation()
    Overfitting()
    LearningCurve()


if __name__ == "__main__":
    main()
