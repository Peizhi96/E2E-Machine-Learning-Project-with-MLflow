from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "01_data_ingestion"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

