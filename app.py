from flask import Flask, render_template, request, jsonify
import pickle 
import pandas as pd
import json

app = Flask(__name__)

taxiDf = pd.read_csv('models/taxi_cleaned_model.csv')
zoneDf = pd.read_csv('models/data/taxi_zones.csv')

hour_dict = dict(taxiDf['hour_in_day'].value_counts())
labels = list(hour_dict.keys())
data = [int(val) for val in hour_dict.values()]

zoneDf = zoneDf[["zone", "LocationID"]]
json_data = zoneDf.to_json(orient='records')

parsed_data = json.loads(json_data)
print(parsed_data)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/prediction')
def predict_page_view():
    return render_template("prediction.html")

@app.route('/zone_data')
def zone_data():
    return jsonify(parsed_data)


@app.route('/visualize')
def visualize_page_view():
    return render_template("visualize.html", labels = labels, data = data)

@app.route('/fare_predict', methods=['POST'])
def fare_predict():
    # Get all the form values and log them to console
    form_values = list(request.form.values())
    print(form_values)

    with open('models/data/dtModel.pkl', 'rb') as f:
        dtModel = pickle.load(f)

    with open('models/data/rfModel.pkl', 'rb') as f:
        rfModel = pickle.load(f)

    input_taxi_data = {
        'passenger_count': form_values[4],
        'trip_distance': form_values[5],	
        'rate_code': form_values[6], 	
        'payment_type':	form_values[7],
        'extra': form_values[8],
        'mta_tax': form_values[9],
        'tip_amount':form_values[10],
        'tolls_amount':	form_values[11],
        'imp_surcharge': form_values[12],	
        'pickup_location_id': form_values[13],
        'dropoff_location_id': form_values[14],
        'hour_in_day':	form_values[0],
        'day':	form_values[2],
        'day_of_week':form_values[1],
        'month': form_values[3],	
        'trip_duration': form_values[15]
    }

    input_df = pd.DataFrame(input_taxi_data, index=[0])
    dtPrediction = dtModel.predict(input_df)[0]
    rfPrediction = rfModel.predict(input_df)[0]

    prediction = round((dtPrediction + rfPrediction) / 2, 3)

    return render_template("fare_predict.html", prediction=prediction, input_data=input_taxi_data)

@app.route('/zones')
def zones_page_view():
    # pass the JSON data to the template
    return render_template('zones.html', json_data=parsed_data)

if __name__ == '__main__':
    app.run(debug=True, port=5003)