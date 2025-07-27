import sys
sys.path.append(r"C:\Gracy_Info\Hexaware\Python Foundation Training - Batch 2\Project\E-commerce")

import pyodbc

driver_name='SQL Server'
server=r'GRACY\SQLEXPRESS'
database='Ecommerce'

class PropertyUtil:
    @staticmethod
    def get_property_string():
        connection_string=f'Driver={driver_name}; Server={server}; Database={database}; Trusted_Connection=yes;'
        return connection_string
