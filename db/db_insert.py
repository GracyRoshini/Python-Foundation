import pyodbc

server = r'GRACY\SQLEXPRESS'
database = 'Student1'
#username = r'GRACY\gracy'
#password = 'yourpassword'            # Replace with your actual password
driver = 'SQL Server'

conn_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("✅ Connected successfully using SQL login!")
except Exception as e:
    print("❌ Connection failed:", e)
