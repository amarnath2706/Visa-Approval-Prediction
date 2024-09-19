import os
from datetime import date

DATABASE_NAME = "VISA_PRED"

COLLECTION_NAME = "DATA_VISA"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "visa_approval"
ARTIFACT_DIR: str = "artifact"


TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "visa_approval.csv"
MODEL_FILE_NAME = "model.pkl"