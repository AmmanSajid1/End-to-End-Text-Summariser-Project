from src.textSummariser.config.configuration import ConfigurationManager
from src.textSummariser.components.model_evaluation import ModelEvauluation
from textSummariser.logging import logger 

class ModelEvaluationTraningPipeline:
    def __init__(self):
        pass 

    def initiate_model_evaluation(self):
        config =ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvauluation(config=model_evaluation_config)
        model_evaluation.evaluate()