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