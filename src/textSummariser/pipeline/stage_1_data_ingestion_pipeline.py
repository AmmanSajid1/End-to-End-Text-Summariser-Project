from src.textSummariser.config.configuration import ConfigurationManager
from src.textSummariser.components.data_ingestion import DataIngestion
from src.textSummariser.logging import logger 

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass 

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingesion = DataIngestion(config=data_ingestion_config)

        data_ingesion.download_file()
        data_ingesion.extract_zip_file()