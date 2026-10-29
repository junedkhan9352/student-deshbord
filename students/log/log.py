import logging

logging.basicConfig(
    filename="students/log/error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(filename)s -%(levelname)s - %(message)s"
)

def log_error(error):
    logging.error(error)