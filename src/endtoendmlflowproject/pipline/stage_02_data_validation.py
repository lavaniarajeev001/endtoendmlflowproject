from src.endtoendmlflowproject.config.configuration import ConfigurationManager
from src.endtoendmlflowproject.components.data_validation import DataValidation
from src.endtoendmlflowproject.logging import logger

STAGE_NAME="Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(data_validation_config)
        data_validation.validation_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e