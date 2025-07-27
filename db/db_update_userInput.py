import pyodbc

server = r'GRACY\SQLEXPRESS'
database = 'Student1'
driver = 'SQL Server'

con_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    print("enter employee info")
    emp_id=int(input('employee id:'))
    emp_name=input('employee name:')
    dept_id=int(input('dept id:'))
    basic_salary=int(input('basic salary:'))
          
    con = pyodbc.connect(con_str)
    cursor=con.cursor()
    str1='update employee set ename=?, dept_id=?, basic_salary=? where eid=?'
    
    cursor.execute(str1,(emp_name,dept_id,basic_salary,emp_id,))
    cursor.commit()
    print("Data updated into employee table")
    
except Exception as e:
    print("Error", e)
