# testing

from src.cnnClassifier import logger 
from src.cnnClassifier.pipeline.stage_01 import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f'>>> stage {STAGE_NAME} started <<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e