import pickle
import pandas as pd

def predict_price_decision_tree():
    # Load the decision tree model from the pickle file
    with open('data/dtModel.pkl', 'rb') as f:
        dtModel = pickle.load(f)

    return dtModel

def predict_price_random_forest():
    with open('data/rfModel.pkl', 'rb') as f:
        rfModel = pickle.load(f)

    return rfModel

def predict_fare(input_data, model):
    """
    Predict the fare amount for a new taxi ride based on the input data and model.
    """
    input_df = pd.DataFrame(input_data, index=[0])
    prediction = model.predict(input_df)[0]
    return prediction

if __name__ == "__main__":
    input_taxi_data = {
        'passenger_count': 2,
        'trip_distance': 10.03,	
        'rate_code': 2, 	
        'payment_type':	2,
        'extra': 0.50,
        'mta_tax': 0.50,
        'tip_amount':0.00,
        'tolls_amount':	0.00,
        'imp_surcharge': 0.30,	
        'pickup_location_id': 150,
        'dropoff_location_id': 56,
        'hour_in_day':	16,
        'day':	26,
        'day_of_week':	4,
        'month': 3,	
        'trip_duration': 618.0	
    }

    dtPredicted = predict_fare(input_taxi_data, predict_price_decision_tree())
    rfPredicted = predict_fare(input_taxi_data, predict_price_random_forest())
    print(dtPredicted)
    print(rfPredicted)
    final_predicted_price = (dtPredicted + rfPredicted) / 2
    print(f'The final avg predicted price is: {final_predicted_price}')