import pandas as pd
import random


def train_test_split(df):
    df = df.reset_index()
    row, col = df.shape
    test_size = round(0.25 * row)
    indices = df.index.tolist()
    test_indices = random.sample(population=indices, k=test_size)

    test_df = df.loc[test_indices]
    train_df = df.drop(test_indices)

    return train_df, test_df


def main():
    df = pd.read_csv("../dataset/CombinedData.csv")
    train, test = train_test_split(df)
    train.to_csv("../dataset/TrainingData.csv")
    test.to_csv("../dataset/TestData.csv")


if __name__ == "__main__":
    main()
