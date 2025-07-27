import pyodbc

server = r'GRACY\SQLEXPRESS'
database = 'Student1'
#username = r'GRACY\gracy'
#password = 'yourpassword'            # Replace with your actual password
driver = 'SQL Server'

con_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

con = pyodbc.connect(con_str)
print("Connection successful!")
