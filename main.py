from networkSecurtiy.components.data_ingestion import Data_Ingestion
from networkSecurtiy.components.data_validation import DataValidation
from networkSecurtiy.exception.exception import NetworkSecurityException
from networkSecurtiy.logging.logger import logging
from networkSecurtiy.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networkSecurtiy.entity.config_entity import TrainingPipelineConfig
import sys


        
if __name__=='__main__':
    try:
        trainingpipelinecongif=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelinecongif)
        data_ingestion=Data_Ingestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("data intitation completed")
        print(dataingestionartifact)
        data_validiation_config=DataValidationConfig(trainingpipelinecongif)
        data_validation=DataValidation(dataingestionartifact,data_validiation_config)
        logging.info("initating data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)


        
    except Exception as e:
           raise NetworkSecurityException(e,sys)