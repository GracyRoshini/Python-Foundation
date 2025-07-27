import pyodbc

driver_name='SQL Server'
server='GRACY\\SQLEXPRESS'
database='LoanDB'

class DBPropertyUtill:
    @staticmethod
    def get_property_string():
        return f'Driver={{{driver_name}}}; Server={server}; Database={database}; Trusted_Connection=yes;'
