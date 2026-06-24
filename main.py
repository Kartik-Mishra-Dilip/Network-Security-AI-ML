from networkSecurtiy.components.data_ingestion import Data_Ingestion
from networkSecurtiy.components.data_validation import DataValidation
from networkSecurtiy.components.model_training import ModelTrainer
from networkSecurtiy.exception.exception import NetworkSecurityException
from networkSecurtiy.logging.logger import logging
from networkSecurtiy.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networkSecurtiy.entity.config_entity import TrainingPipelineConfig
from networkSecurtiy.components.data_transformation import DataTransformation
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
        data_transform_config=DataTransformationConfig(trainingpipelinecongif)
        logging.info("data transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transform_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation completed")


        logging.info("model training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelinecongif)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("model training  artifact created")

        
    except Exception as e:
           raise NetworkSecurityException(e,sys)