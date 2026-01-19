from loguru import logger
import sys


def get_logger(name: str):
    logger.remove()
    logger.add(sys.stdout, format="<green>{time}</green> | <level>{level}</level> | {message}")
    return logger.bind(module=name)
