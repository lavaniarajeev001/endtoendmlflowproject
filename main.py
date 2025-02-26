from src.endtoendmlflowproject.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.endtoendmlflowproject.logging import logger
from src.endtoendmlflowproject.pipline.stage_02_data_validation import DataValidationPipeline
from src.endtoendmlflowproject.pipline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.endtoendmlflowproject.pipline.stage_04_model_trainer import ModelTrainingPipeline
from src.endtoendmlflowproject.pipline.stage_05_ModelEvaluation import ModelEvaluationPipeline


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

STAGE_NAME= "Model Trainer Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    Model_trainer=ModelTrainingPipeline()
    Model_trainer.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Model Evaluation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    Model_Evaluation=ModelEvaluationPipeline()
    Model_Evaluation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e
