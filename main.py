from networkSecurtiy.components.data_ingestion import Data_Ingestion
from networkSecurtiy.exception.exception import NetworkSecurityException
from networkSecurtiy.logging.logger import logging
from networkSecurtiy.entity.config_entity import DataIngestionConfig
from networkSecurtiy.entity.config_entity import TrainingPipelineConfig
import sys


        
if __name__=='__main__':
    try:
        trainingpipelinecongif=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelinecongif)
        data_ingestion=Data_Ingestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

        
    except Exception as e:
           raise NetworkSecurityException(e,sys)