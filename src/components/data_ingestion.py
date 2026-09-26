import sys
import os
from src.logger import logging
from src.exceptions import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


from src.components.data_transformation import DataTransformationConfig, DataTransformation
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

@dataclass # this decorator is used to automatically generate special methods like
#__init__() and __repr__() for the class based on the defined attributes.
class DataIngestionConfig:
    # Define the paths for train, test, and raw data files
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        try:
            # Read the dataset from the specified path
            # Normally this would be from an external source or a database, but here it's hardcoded for demonstration purposes.
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")

            # Create the artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)


            # Save the raw data to a CSV file
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")

            # Split the dataset into training and testing sets (80% train, 20% test)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training and testing sets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


# to test
if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_path, test_path)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr, preprocessor_path=data_transformation.data_transformation_config.preprocessor_obj_file_path))