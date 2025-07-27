#Abstract class

"""
1) Always act as base class
   We cannot create Object to the abstract class
2) Declaration the variables, function(cannot define)
3) Derived class should have the function definition of the abstract method
4) Import abstract package(ABC)
"""

from abc import *
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

#derived1
class sbi(Bank):
    def interest(self):
        roi=10
        print('SBI interest rate: ',roi)

#derived2
class Indian_bank(Bank):
    def interest(self):
        roi=20
        print('Indian bank rate of interest: ',roi)

sobj=sbi()
iobj=Indian_bank()
sobj.interest()
iobj.interest()
