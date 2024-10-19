import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create the detailed error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # Initialize the parent class with the error string
        # Call error_message_detail to get a detailed error message
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message


# Main block
if __name__ == "__main__":
    logging.info("Logging has started")

    try:
        # Deliberately trigger division by zero error
        a = 1 / 0

    except Exception as e:
        logging.error("Division by zero error occurred")  # Use logging.error to log the error
        # Raise custom exception with detailed error information
        raise CustomException(e, sys)
