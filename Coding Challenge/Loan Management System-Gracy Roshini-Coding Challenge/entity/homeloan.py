from loan import Loan

class HomeLoan(Loan):
    def __init__(self, property_address=None, property_value=None, **kwargs):    #--Accept all other parameters that belong to the parent class Loan
        super().__init__(**kwargs)    #--to pass those remaining parameters to the parent class's constructor
        self.property_address=property_address
        self.property_value=property_value

    def __str__(self):
        return super().__str__() + f", Property Address: {self.property_address}, Value: {self.property_value}"
    
