import os
import sys
import logging

# Logging format
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

# Directory and file setup
log_dir = "logs"
log_filepath = os.path.join(log_dir, "cnnClassifier.log")
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,  # lowercase 'level'
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger instance
logger = logging.getLogger("cnnClassifierLogger")
