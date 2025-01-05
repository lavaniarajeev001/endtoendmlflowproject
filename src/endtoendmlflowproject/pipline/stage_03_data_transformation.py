from src.endtoendmlflowproject.config.configuration import ConfigurationManager
from src.endtoendmlflowproject.components.data_transformation import DataTransformation
from src.endtoendmlflowproject.logging import logger
from pathlib import Path


STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            data_transformation_config=config.get_data_transformation()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
        except Exception as e:
            print(e) 

if __name__=="__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
        