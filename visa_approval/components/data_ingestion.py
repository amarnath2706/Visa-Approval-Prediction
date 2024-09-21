import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from visa_approval.entity.config_entity import DataIngestionConfig
from visa_approval.entity.artifact_entity import DataIngestionArtifact
from visa_approval.exception import visaException
from visa_approval.logger import logging
from visa_approval.data_access.visa_data import VisaData

#Class for dataingestion
class DataIngestion:
    #here it taking the data ingestion configuration
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise visaException(e,sys)

#Method to export the data into feature store
def export_data_into_feature_store(self)->DataFrame:
        """
        Method Name :   export_data_into_feature_store
        Description :   This method exports data from mongodb to csv file
        
        Output      :   data is returned as artifact of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            logging.info(f"Exporting data from mongodb")
            usvisa_data = VisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=
                                                                   self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            feature_store_file_path  = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
            raise visaException(e,sys)