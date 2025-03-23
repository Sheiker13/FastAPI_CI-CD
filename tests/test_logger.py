import os
from app.logger import logger

def test_logger_writes_file():
    test_message = "Test log message"
    logger.info(test_message)
    log_path = "logs/app.log"
    assert os.path.exists(log_path), "Log file does not exist"
    with open(log_path, "r") as f:
        contents = f.read()
    assert test_message in contents