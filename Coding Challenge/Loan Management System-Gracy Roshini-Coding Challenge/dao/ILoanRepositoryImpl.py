
import sys
sys.path.append(r"C:\Gracy_Info\Hexaware\Python Foundation Training - Batch 2\Coding Challenge\Loan Management System")

import pyodbc
from dao.ILoanRepository import ILoanRepository
from entity.loan import Loan
from entity.customer import Customer
from exception.InvalidLoanException import InvalidLoanException
from exception.LowPaymentException import LowPaymentException
from utill.DBConnUtill import DBConnUtill

class ILoanRepositoryImpl(ILoanRepository):

    def __init__(self):
        self.conn=DBConnUtill.get_connection()

    def applyLoan(self,loan):
        a=input("Do you want to apply for this loan? yes or no: ").strip().lower()
        if a!='yes':
            print("Loan application cancelled")
            return

        cursor= self.conn.cursor()
        query="""Insert into Loans( customerId, principalAmount, interestRate, LoanTerm, loanType, loanStatus) Values(?,?,?,?,?,?)"""
        cursor.execute(query, loan.customer.get_customer_id(), loan.principal_amount,
                       loan.interest_rate, loan.loan_term, loan.loan_type, loan.loan_status)
        self.conn.commit()
        print("Loan applied Successfully!")

    def getLoanById(self,loan_id):
        cursor=self.conn.cursor()
        cursor.execute("Select * from Loans where loanId=?",loan_id)
        row=cursor.fetchone()
        if not row:
            raise InvalidLoanException()
        print(row)

    def calculateInterestOverload(self, principal, rate, tenure):
        return (principal*rate*tenure)/1200

    def calculateEMIOverload(self,principal,rate,tenure):
        r=rate/12/100
        emi=(principal*r*(1+r)**tenure)/((1+r)**tenure-1)
        return round(emi,2)
    
    def calculateInterest(self,loan_id):pass

    def loanStatus(self,loan_id): pass

    def calculateEMI(self,loan_id):pass

    def loanRepayment(self, loan_id, amount):pass

    def getAllLoan(self):pass
    
