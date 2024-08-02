# testing stage_01

from src.cnnClassifier import logger 
from src.cnnClassifier.pipeline.stage_01 import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f'>>> stage {STAGE_NAME} started <<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


# testing stage_02
STAGE_NAME = "Prepare base model"
try:
    logger.info(f"*******************")
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(">>> stage {STAGE_NAME} completed <<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e