class LowPaymentException(Exception):
    def __init__(self,message="Payment too low to cover one EMI"):
        super().__init__(message)
