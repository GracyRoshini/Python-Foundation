from entity.customer import Customer

class Loan:
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None, loan_type=None, loan_status="Pending"):
        self.loan_id=loan_id
        self.customer=customer
        self.principal_amount=principal_amount
        self.interest_rate=interest_rate
        self.loan_term=loan_term
        self.loan_type=loan_type
        self.loan_status=loan_status

    def __str__(self):
        return f"LoanID: {self.loan_id}, Customer: [{self.customer}], Amount: {self.principal_amount}, Rate: {self.interest_rate}, Term: {self.loan_term}, Type: {self.loan_type}, Status: {self.loan_status}"
