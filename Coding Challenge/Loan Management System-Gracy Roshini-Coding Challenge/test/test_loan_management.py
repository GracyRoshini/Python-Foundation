import unittest
import sys
import uuid

sys.path.append(r"C:\Gracy_Info\Hexaware\Python Foundation Training - Batch 2\Coding Challenge\Loan Management System-Gracy Roshini-Coding Challenge")

from dao.ILoanRepositoryImpl import ILoanRepositoryImpl
from entity.customer import Customer
from entity.loan import Loan
from exception.InvalidLoanException import InvalidLoanException

class TestLoanManagementSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo=ILoanRepositoryImpl()

    def test_apply_loan_success(self):
        cust=Customer(1,"Test User","testuser@example.com","1234567890","City",700)
        loan=Loan(None,cust,100000,7.0,12,"HomeLoan","Pending")

        input_values=['yes']
        def mock_input(_):
            return input_values.pop(0)
        original_input=__builtins__.input
        __builtins__.input=mock_input

        try:
            self.repo.applyLoan(loan)
        finally:
            __builtins__.input=original_input


    def test_calculate_interest_overload(self):
        result=self.repo.calculateInterestOverload(100000,7.5,12)
        expected=(100000*7.5*12)/1200
        self.assertEqual(result, expected)

    def test_calculate_emi_overload(self):
        result=self.repo.calculateEMIOverload(100000,7.5,12)
        self.assertIsInstance(result,float)
        self.assertGreater(result,0)

    def test_get_loan_by_id_success(self):
        try:
            self.repo.getLoanById(1)
        except InvalidLoanException:
            self.fail("Loan with ID 1 should exist for this test")

    def test_get_loan_by_id_failure(self):
        with self.assertRaises(InvalidLoanException):
            self.repo.getLoanById(99999)

if __name__=="__main__":
    unittest.main()
        
