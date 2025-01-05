from src.endtoendmlflowproject.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.endtoendmlflowproject.logging import logger
from src.endtoendmlflowproject.pipline.stage_02_data_validation import DataValidationPipeline
from src.endtoendmlflowproject.pipline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    Data_ingestion = DataIngestionTrainingPipeline()
    Data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e

STAGE_NAME="Data Validation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation=DataValidationPipeline()
    data_validation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e
