import os
import sys

import numpy as np
import pandas as pd
import dill
import pickle

from sklearn.metrics import r2_score
from src.logger import logging
from src.exceptions import CustomException



# to save an object as a pickle file
def save_object(file_path, obj):
    try:
        logging.info("Entered the save_object method of utils")
        # Create the directory if it doesn't exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Save the object as a pickle file
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Object has been saved successfully")
    except Exception as e:
        raise CustomException(e, sys)



# to evaluate multiple models and return their performance scores
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        logging.info("Entered the evaluate_models method of utils")
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            model_name = list(models.keys())[i]

            # Fit the model on the training data
            model.fit(X_train, y_train)

            #predict on the training data
            y_train_pred = model.predict(X_train)
    
            # Predict on the test data
            y_test_pred = model.predict(X_test)


            # Calculate the R2 score and store it in the report dictionary
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        logging.info("Model evaluation completed successfully")
        return report

    except Exception as e:
        raise CustomException(e, sys)