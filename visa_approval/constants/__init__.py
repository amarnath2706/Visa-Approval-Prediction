import os
from datetime import date

#Database Name
DATABASE_NAME = "VISA_PRED"
#Collection name
COLLECTION_NAME = "DATA_VISA"
MONGODB_URL_KEY = "MONGODB_URL"
#Pipeline name
PIPELINE_NAME: str = "visa_approval"
#name of the artifact directory
ARTIFACT_DIR: str = "artifact"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
#File name 
FILE_NAME: str = "visa_approval.csv"
#Model name
MODEL_FILE_NAME = "model.pkl"

#validation
TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

#Evaluation
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

#Data ingestion related constants
DATA_INGESTION_COLLECTION_NAME: str = "DATA_VISA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion" #it will Create the folder inside the artifact directory
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" #it will Create the folder inside the artifact directory
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2 #train-test split ratio


#Data validation related constants

DATA_VALIDATION_DIR_NAME: str = "data_validation" #it will Create the folder inside the artifact directory
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report" #it will Create the folder inside the artifact directory
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

#Data transformation related constants

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation" #it will Create the folder inside the artifact directory
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

#Model Trainer constants

MODEL_TRAINER_DIR_NAME: str = "model_trainer" #it will Create the folder inside the artifact directory
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6 #How much score we expect from our model
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")

#Model Evaluation constants

MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02 #Set the threshold to your wish, in the production set threhold = 0.07
MODEL_BUCKET_NAME = "visa-model2024"
MODEL_PUSHER_S3_KEY = "model-registry"


APP_HOST = "0.0.0.0"
APP_PORT = 8080

