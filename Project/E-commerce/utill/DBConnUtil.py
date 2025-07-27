import pyodbc

import sys
sys.path.append(r'C:\Gracy_Info\Hexaware\Python Foundation Training - Batch 2\Project\E-commerce')

from utill.PropertyUtil import PropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        connection_string=PropertyUtil.get_property_string()
        return pyodbc.connect(connection_string)
