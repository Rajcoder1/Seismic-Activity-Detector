from flask import Flask, render_template, jsonify
import csv
import time

app = Flask(__name__)

# Load the data from CSV just once when the app starts
def read_csv_data():
    with open('xa.s12.00.mhz.1970-01-19HR00_evid00002.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = [{"time": row["time_rel(sec)"], "value": row["velocity(m/s)"]} for row in reader]
    return data

data = read_csv_data()

# Serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# API route to send one data point at a time
@app.route('/get_data/<int:index>')
def get_data(index):
    if index < len(data):
        return jsonify(data[index])
    else:
        return jsonify({})  # No more data points

if __name__ == '__main__':
    app.run(debug=True)
