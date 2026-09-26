import os
import sys

import numpy as np
import pandas as pd
import dill
import pickle
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