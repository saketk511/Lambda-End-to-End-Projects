import logging
import os
from datetime import datetime

# Generate a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory path for storing log files within the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the 'logs' directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Set the log message format
    level=logging.INFO,  # Set the logging level to INFO
)

