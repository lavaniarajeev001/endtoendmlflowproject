from src.endtoendmlflowproject.config.configuration import ConfigurationManager
from src.endtoendmlflowproject.components.model_evaluation import ModelEvaluation
from src.endtoendmlflowproject.logging import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init_(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__=="__main__":
    logger.info("Model Training Pipeline Started")
    obj=ModelEvaluationPipeline()
    obj.main()
    logger.info("Model Training Pipeline Ended")