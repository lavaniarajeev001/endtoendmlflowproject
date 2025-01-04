from src.endtoendmlflowproject.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.endtoendmlflowproject.logging import logger


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e
