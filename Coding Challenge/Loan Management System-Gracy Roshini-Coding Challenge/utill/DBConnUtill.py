import pyodbc
from utill.DBPropertyUtill import DBPropertyUtill

class DBConnUtill:
    @staticmethod
    def get_connection():
        connection_string = DBPropertyUtill.get_property_string()
        return pyodbc.connect(connection_string)
