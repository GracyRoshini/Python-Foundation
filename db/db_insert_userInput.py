import pyodbc

server = r'GRACY\SQLEXPRESS'
database = 'Student1'
#username = r'GRACY\gracy'
#password = 'yourpassword'            # Replace with your actual password
driver = 'SQL Server'

con_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    print("enter employee info")
    emp_id=int(input('employee id:'))
    emp_name=input('employee name:')
    dept_id=int(input('dept id:'))
    basic_salary=int(input('basic salary:'))
          
    con = pyodbc.connect(con_str)
    curosr=con.cursor()
    str1='insert into employee(eid,ename,dept_id,basic_salary) values(?,?,?,?)'
    curosr.execute(str1,(emp_id,emp_name,dept_id,basic_salary))
    curosr.commit()
    print("Data inserted into employee table")
except Exception as e:
    print("Error", e)
