import sys
from visa_approval.exception import USvisaException
from visa_approval.logger import logging
from visa_approval.components.data_ingestion import DataIngestion

#import config entity and artifact entity

from visa_approval.entity.config_entity import (DataIngestionConfig)

from visa_approval.entity.artifact_entity import (DataIngestionArtifact)