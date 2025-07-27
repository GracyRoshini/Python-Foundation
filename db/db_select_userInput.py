import pyodbc

server = r'GRACY\SQLEXPRESS'
database = 'Student1'
driver = 'SQL Server'

con_str = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    salary=int(input('enter employee eid'))   
    con = pyodbc.connect(con_str)
    cursor=con.cursor()
    str1='select * from employee where eid=?'
    cursor.execute(str1,(salary))
    res=cursor.fetchone()

    if res:
        for i in res:
            print(i)
    else:
        print("no emp found w given basic salary!")

    cursor.close()
    con.close()


except Exception as e:
    print("Error", e)
