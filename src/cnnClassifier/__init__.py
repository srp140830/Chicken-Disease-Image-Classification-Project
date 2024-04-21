# This is custom logging

import os
import sys
import logging # importing logging module

logging_str = '[%(asctime)s : %(levelname)s: %(module)s: %(message)s]'

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # for pushing the logs on to the file
        logging.StreamHandler(sys.stdout) # For pushing the logs on to the console
    ]

)

logger = logging.getLogger("cnnClassifierLogger")