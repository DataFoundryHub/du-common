import logging
import json
from utils import create_logger
def create_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger


def json_reader(path):
    with open(path, 'r') as file:
        config = json.load(file)
    return config
