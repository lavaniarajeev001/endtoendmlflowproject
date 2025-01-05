from src.endtoendmlflowproject.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.endtoendmlflowproject.logging import logger
from src.endtoendmlflowproject.pipline.stage_02_data_validation import DataValidationPipeline


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e

STAGE_NAME="Data Validation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj=DataValidationPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e
