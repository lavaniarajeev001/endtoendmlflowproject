from src.endtoendmlflowproject.config.configuration import ConfigurationManager
from src.endtoendmlflowproject.components.model_trainer import ModelTrainer
from src.endtoendmlflowproject.logging import logger

STAGE_NAME= "Model Trainer Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__ == "__main__":
    logger.info("Model Training Pipeline Started")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info("Model Training Pipeline Ended")