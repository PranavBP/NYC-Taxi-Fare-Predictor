from flask import Flask, render_template, request, jsonify
import pickle 
import pandas as pd
import json

app = Flask(__name__)

taxiDf = pd.read_csv('models/taxi_cleaned_model.csv')
taxi2Df = pd.read_csv('models/taxi_cleaned.csv')
print(len(taxi2Df))
taxiDf = taxiDf.sample(frac = 0.25, replace = False, random_state = 1)
taxiDf = taxiDf.reset_index(drop = True)

zoneDf = pd.read_csv('models/data/taxi_zones.csv')

hour_dict = dict(taxiDf['hour_in_day'].value_counts())
labels = list(hour_dict.keys())
data = [int(val) for val in hour_dict.values()]

fare_amounts = list(taxiDf['fare_amount'])
trip_distances = list(taxiDf['trip_distance'])



location_count = taxiDf['dropoff_location_id'].value_counts().reset_index()
location_count.columns = ['dropoff_location_id', 'count']
location_count



zoneDf = zoneDf[["zone", "LocationID"]]
json_data = zoneDf.to_json(orient='records')

parsed_data = json.loads(json_data)

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
    return render_template("visualize.html", labels = labels, data = data, fare_amounts=fare_amounts, trip_distances=trip_distances)

@app.route("/line_plot")
def line_plot():
    hourly_fare_amount = taxi2Df.groupby(["months", "hour_in_day"])["fare_amount"].mean().reset_index()
    months = hourly_fare_amount["months"].unique()
    chart_data = {}
    for month in months:
        chart_data[str(month)] = hourly_fare_amount[hourly_fare_amount["months"] == month][["hour_in_day", "fare_amount"]].to_dict("list")
    return jsonify(chart_data)

@app.route('/polar_plot')
def polar_plot():
    polar_data = location_count.to_dict(orient='records')
    return jsonify(polar_data)

@app.route('/day_pie_chart_data')
def day_pie_chart_data():
    dayDict = dict(taxi2Df['day_in_week'].value_counts())
    day_data = list(dayDict.values())
    day_labels = list(dayDict.keys())
    chart_data = {'day_data': day_data, 'day_labels': day_labels}
    json_data = json.dumps(chart_data, default=str)
    return json_data


@app.route('/radar_data')
def radar_data():
    groupedData = taxi2Df.groupby(['rate_code_dest'])['fare_amount'].mean()
    data_dict = {'rate_code_dest': groupedData.index.tolist(), 'fare_amount': groupedData.tolist()}
    return jsonify(data_dict)


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
        'passenger_count': form_values[2],
        'trip_distance': form_values[3],	
        'rate_code': form_values[4], 	
        'payment_type':	form_values[5],
        'mta_tax': form_values[6],
        'tip_amount':form_values[7],
        'tolls_amount':	form_values[8],
        'imp_surcharge': form_values[9],	
        'pickup_location_id': form_values[10],
        'dropoff_location_id': form_values[11],
        'hour_in_day':	form_values[0],
        'day_of_week':form_values[1],	
        'trip_duration': form_values[12]
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
    app.run(debug=True, port=5002)