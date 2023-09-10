# app.py
import pandas as pd
from flask import Flask, render_template, request, jsonify
from database import insert_customer_data  # Import your database function

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    # Your index.html rendering logic here
    return render_template('index.html')


@app.route('/client_form')
def client_form():
    # Your client_form.html rendering logic here
    return render_template('client_form.html')


@app.route('/save_client', methods=['POST'])
def save_client():
    data = request.get_json()
    insert_customer_data(data)

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Specify the full path for saving the Excel file
    file_path = '/home/anand/PycharmProjects/Project/Records/client_data.xlsx'

    # Save the DataFrame to the specified path, overwriting any existing data
    df.to_excel(file_path, index=False)

    return jsonify({"message": "Data saved successfully"})

@app.route('/add', methods=['GET'])
def add_client():
    return render_template('client_form.html')


if __name__ == '__main__':
    app.run(debug=True)
