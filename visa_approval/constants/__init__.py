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

#Data ingestion related constants
DATA_INGESTION_COLLECTION_NAME: str = "DATA_VISA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion" #it will Create the folder inside the artifact directory
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
