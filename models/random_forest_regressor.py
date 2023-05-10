import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def random_forest_regressor():
    taxiDf = pd.read_csv('taxi_cleaned_model.csv')
    X = taxiDf.drop(['fare_amount'], axis=1)
    y = taxiDf['fare_amount']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
    rfModel = RandomForestRegressor(n_estimators = 100, random_state = 1)
    rfModel.fit(x_train, y_train)  

    print('train score :', rfModel.score(x_train, y_train))
    print('test score :', rfModel.score(x_test, y_test))

    # Save the model to a pickle file
    with open('data/rfModel.pkl', 'wb') as f:
        pickle.dump(rfModel, f)
        print("Random Forest Regression model built successfully")

if __name__ == "__main__":
    random_forest_regressor()





