from flask import Flask, jsonify
import pandas as pd
import os
from lib.paths import get_base_path
from lib.pandas_database_functions import queryCSV
from flask_cors import CORS  # Import CORS extension
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/send_translated', methods=['GET'])
def send_translated():
    try:
        # Assuming the CSV file is named 'data.csv' and in the same directory as this script
        datasets_folder="datasets"
        raw_messages_file_path = os.path.join(get_base_path(__file__), datasets_folder, 'translated_words.csv')
        # Read the CSV file into a DataFrame
        df = queryCSV(raw_messages_file_path)
        # Convert the DataFrame to a list of dictionaries (each row as a dictionary)
        data_array = df.to_dict(orient='records')
        # Make keys lowercase
        lowercase_data_array = []
        for data in data_array:
            lowercase_data = {key.lower(): value for key, value in data.items()}
            lowercase_data_array.append(lowercase_data)

        return jsonify({'message':'translated word data successfully retrieved','data':lowercase_data_array})
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return the error message and status code 500 for internal server error

if __name__ == '__main__':
    app.run()
