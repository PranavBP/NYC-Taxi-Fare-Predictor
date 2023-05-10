import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt 
color_pal = sns.color_palette("hls")
pd.set_option('display.max_columns', 30)
import pickle
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


def decision_tree_regressor():
    taxiDf = pd.read_csv('taxi_cleaned_model.csv')
    X = taxiDf.drop(['fare_amount'], axis=1)
    y = taxiDf['fare_amount']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    # Train the decision tree regression model on the training set
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    # Save the model to a pickle file
    with open('data/dtModel.pkl', 'wb') as f:
        pickle.dump(model, f)
        print("Decision Tree model built successfully")

if __name__ == "__main__":
    decision_tree_regressor()