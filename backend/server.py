from flask import Flask, jsonify,send_file,request
import pandas as pd
import os
from lib.paths import get_base_path
from lib.pandas_database_functions import queryCSV
from flask_cors import CORS  # Import CORS extension
from gtts import gTTS  
from subprocess import run
from dotenv import load_dotenv
from celery import Celery

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

from flask import request
load_dotenv()
redis_server = os.getenv('REDIS_SERVER')

celery_app = Celery(
    'tasks',
    broker=redis_server,  # Replace with your Redis server details
    backend=redis_server  # Replace with your Redis server details
)

# Set up Celery configuration
celery_app.conf.update(
    result_expires=36000,
)
@app.route('/trigger_job_dispatch', methods=['GET'])
def trigger_job_dispatch():
    try:
        # Dispatch the tasks to the queue
        #celery_app.send_task('tasks.execute_script', args=('R01-churn.py',))
        #celery_app.send_task('tasks.execute_script', args=('R02-extractWords.py',))
        celery_app.send_task('tasks.execute_script', args=('R03-translate.py',))
        
        return jsonify({"message": "Scripts triggered successfully"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@celery_app.task(name='tasks.execute_script')
def execute_script(script_name):
    try:
        routines_folder = "routines"
        routine_file_path = os.path.join(get_base_path(__file__), routines_folder, script_name)
        
        # Run the Python script here
        run(["python", routine_file_path])
        
        # Use a notification mechanism to inform about completion
        # Notify through a webhook, database update, or messaging system
    except Exception as e:
        # Handle exceptions or errors
        pass

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

@app.route('/pronunciation', methods=['POST'])
def pronunciation():
    try:
        audio_folder = "audio"
        audio_path = os.path.join(get_base_path(__file__), audio_folder, 'audio.csv')
        # Parse the data from the POST request
        translated_text = request.form.get('translated_text')
        out_lang = request.form.get('out_lang')
        speak = gTTS(text=translated_text, lang=out_lang, slow=False)
        speak.save(audio_path)
        return send_file(audio_path, mimetype='audio/mpeg')
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return the error message and status code 500 for internal server error

@app.route('/check_task_status/<task_id>')
def check_task_status(task_id):
    task = celery_app.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        # Task completed successfully
        # Add your notification or logging mechanism here
        return jsonify({'status': 'Task completed'})
    elif task.state == 'FAILURE':
        # Task failed
        # Handle failure or trigger a retry, etc.
        return jsonify({'status': 'Task failed'})
    else:
        # Task is still pending or in progress
        return jsonify({'status': 'Task in progress'})
    
if __name__ == '__main__':
    app.run()


