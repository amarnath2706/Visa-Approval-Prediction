import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from visa_approval.entity.config_entity import DataIngestionConfig
from visa_approval.entity.artifact_entity import DataIngestionArtifact
from visa_approval.exception import USvisaException
from visa_approval.logger import logging
from visa_approval.data_access.visa_data import VisaData