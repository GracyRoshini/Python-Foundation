from abc import ABC, abstractmethod

class ILoanRepository(ABC):

    @abstractmethod
    def applyLoan(self, loan): pass
    
    def getLoanById(self, loan_id):pass
    
    def calculateInterestOverload(self, principal, rate, tenure):pass
    
    def calculateInterestOverload(self, principal, rate, tenure):pass

    #def calculateInterest(self, loan_id):pass

    #def loanStatus(self, loan_id):pass

    #def calculateEMI(self, loan_id):pass

    #def loanRepayment(self, loan_id, amount):pass

    #def getAllLoan(self):pass

