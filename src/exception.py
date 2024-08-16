import sys

# Function to capture detailed error message
def error_message_detail(error, error_detail: sys):
    # Get the traceback object from the exception details
    _, _, exc_tb = error_detail.exc_info()
    # Extract the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Construct the error message with filename, line number, and error details
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class to handle exceptions with detailed error messages
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent class (Exception) constructor
        super().__init__(error_message)
        # Generate and store the detailed error message
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        # Return the detailed error message when the exception is printed
        return self.error_message
