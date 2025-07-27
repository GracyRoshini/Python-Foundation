     
class Customer:
    def __init__(self, customer_id=None, name=None, email_address=None, phone_number=None, address=None, credit_score=None):
        self.__customer_id = customer_id
        self.__name = name
        self.__email_address = email_address
        self.__phone_number = phone_number
        self.__address = address
        self.__credit_score = credit_score

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, value):
        self.__customer_id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_email_address(self):
        return self.__email_address

    def set_email_address(self, value):
        self.__email_address = value

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, value):
        self.__phone_number = value

    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value

    def get_credit_score(self):
        return self.__credit_score

    def set_credit_score(self, value):
        self.__credit_score = value

    def __str__(self):
        return (f"CustomerID: {self.__customer_id}, Name: {self.__name}, "
                f"Email: {self.__email_address}, Phone: {self.__phone_number}, "
                f"Address: {self.__address}, CreditScore: {self.__credit_score}")
        
