import os
import sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))



from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_trainer import Training
from src.cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()#method creates TrainingConfig instance with desired config data(returns training_config)
        training = Training(config=training_config) #creates an instance of Training using TrainingConfig instance previously created
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        

if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e