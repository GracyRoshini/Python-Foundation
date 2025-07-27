class Customers:
    def __init__(self, customer_id=None, name='', email='', password=''): #--constructors
        self.__customer_id = customer_id
        self.__name=name
        self.__email=email
        self.__password = password

    def get_customer_id(self):    #--getter
        return self.__customer_id  
    def set_customer_id(self, cid):    #--setter, pass arguments
        self.__customer_id=cid

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name_id=name

    def get_email(self):
        return self.__email
    def set_email(self, name):
        self.__email=email

    def get_password(self):
        return self.__password
    def set_password(self, pwd):
        self.__password = pwd
