import sys # this is for the exception handling in the code. It allows us to access system-specific parameters and functions, which can be useful for debugging and error reporting.
from src.logger import logging # this is for logging purposes. It allows us to log messages, which can be helpful for tracking the flow of the program and diagnosing issues.

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # this line retrieves the current exception information, including the traceback object, which contains details about where the exception occurred in the code.
    
    file_name = exc_tb.tb_frame.f_code.co_filename # this line extracts the filename from the traceback object, which indicates where the exception was raised.
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error) # this line formats a detailed error message that includes the filename, line number, and the actual error message.
    )
    return error_message


class CustomException(Exception): # this line defines a custom exception class that inherits from the built-in Exception class. It allows us to create our own exception types with additional functionality.
    def __init__(self, error_message, error_detail:sys): # this is the constructor method for the CustomException class. It initializes the exception with a custom error message and additional error details.
        super().__init__(error_message) # this line calls the constructor of the base Exception class to initialize the exception with the provided error message.
        self.error_message = error_message_detail(error_message, error_detail=error_detail) # this line generates a detailed error message using the error_message_detail function and stores it in an instance variable.

    def __str__(self): # this method defines how the CustomException object should be represented as a string. It is called when the exception is printed or converted to a string.
        return self.error_message # this line returns the detailed error message when the CustomException object is converted to a string.

