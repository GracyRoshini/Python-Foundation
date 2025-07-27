import sys

sys.path.append(r"C:\Gracy_Info\Hexaware\Python Foundation Training - Batch 2\Coding Challenge\Loan Management System-Gracy Roshini-Coding Challenge")

from dao.ILoanRepositoryImpl import ILoanRepositoryImpl
from entity.loan import Loan
from entity.customer import Customer

if __name__=="__main__":
    repo=ILoanRepositoryImpl()

    while True:
        print("\n----------Loan Management System----------")
        print("1. Apply for Loan")
        print("2. Get Loan by ID")
        print("3. Calculate EMI (Overloaded)")
        print("4. Calculate Interest (Overloaded)")
        print("5. Exit")

        ch=input(" Enter your choice: ")

        if ch=='1':
            cust=Customer(1,'abc','abc@gmail.com','9876543210','Chennai',800)
            loan=Loan(101,cust,500000,7.5,60,"HomeLoan", "pending")
            repo.applyLoan(loan)

        elif ch=='2':
            loan_id=int(input("Enter Loan ID: "))
            try:
                repo.getLoanById(loan_id)
            except Exception as e:
                print(e)

        elif ch=='3':
            p=float(input("Enter principal:"))
            r=float(input("Enter rate: "))
            t=int(input("Enter tenure in months: "))
            print("EMI: ",repo.calculateEMIOverload(p,r,t))


        elif ch=='4':
            p=float(input("Enter principal: "))
            r=float(input("Enter rate: "))
            t=int(input("Enter tenure in months: "))
            print("Interest: ", repo.calculateInterestOverload(p,r,t))

        elif ch=='5':
            print("Thank you for using Loan Management System!")
            break
        
        else:
            print("Invalid Choice X")
