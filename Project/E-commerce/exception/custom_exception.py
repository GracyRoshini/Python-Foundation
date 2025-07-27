class CustomException(Exception):
    def __init__(self, message="Error Occured"):
        super().__init__(message)
