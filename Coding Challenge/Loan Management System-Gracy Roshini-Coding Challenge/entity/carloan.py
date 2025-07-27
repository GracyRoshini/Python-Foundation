from loan import Loan

class CarLoan(Loan):
    def __init__(self, car_model=None, car_value=None, **kwargs):    #--Accept all other parameters that belong to the parent class Loan
        super().__init__(**kwargs)    #--to pass those remaining parameters to the parent class's constructor
        self.car_model=car_model
        self.car_value=car_value

    def __str__(self):
        return super().__str__() + f", Car Model: {self.car_model}, Car Value: {self.car_value}"
    
