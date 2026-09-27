# Main entry point for the application

import pickle
from flask import Flask, request, jsonify, render_template

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Create a Flask application instance
app = Flask(__name__) # Gives the name of the current module (__name__) to the Flask application instance. This is used to determine the root path of the application and locate resources.

# Define a route for the root URL ('/') of the application
@app.route('/') 
def index():
    return render_template('index.html') 


# Define a route for the '/predictdata' URL of the application, which handles both GET and POST requests
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    # Handle GET requests by rendering the 'home.html' template
    if request.method=='GET':
        return render_template('home.html')

    # Handle POST requests by processing the form data submitted by the user
    else:
        data=CustomData(
            # Collect input data from the form submitted by the user and create an instance of the CustomData class
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))

        )
        # Get the input data as a pandas DataFrame using the get_data_as_data_frame method of the CustomData class
        pred_df=data.get_data_as_data_frame()
        # Print the input DataFrame for debugging purposes
        print(pred_df)
        print("Before Prediction")

        # Create an instance of the PredictPipeline class and use it to make predictions on the input data
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")

        # Make predictions using the predict method of the PredictPipeline class
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")

        # Return the prediction results to the 'home.html' template for display
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":  # Check if the script is being run directly (not imported as a module)
    app.run(host="0.0.0.0", port=5000, debug=True)  # Start the Flask development server on all available network interfaces (host="0.0.0.0")
    # to access the app on chrome, use the following URL: http://localhost:5000/ or http://localhost:5000/predictdata