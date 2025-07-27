class SalaryError(Exception):
    def __init__(self,salary,message='salary is lesser than 50000'):
        self.message=message
        self.salary=salary
        super().__init__(self.message)

salary=int(input("enter salary"))
if salary<50000:
    raise SalaryError(salary)
