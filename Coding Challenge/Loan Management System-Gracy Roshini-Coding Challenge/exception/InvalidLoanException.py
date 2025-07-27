class InvalidLoanException(Exception):
    def __init__(self,message="Loan ID not found"):
        super().__init__(message)
