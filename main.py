# testing stage_01
import os
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/neopinp/End-to-End-Chest-Cancer-Classification-Using-MLflow-DVC.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "neopinp"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "589405f077784a316694430913e805864d0902de"

from src.cnnClassifier import logger 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


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


#Stage_03
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


#Stage_04
STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f"************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
