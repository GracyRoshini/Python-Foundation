class CartEmptyException(Exception):
    def __init__(self, message="Cart is empty"):
        super().__init__(message)
