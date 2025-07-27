#python -m pip install b4
#python -m pip install BeautifulSoup
#python -m pip install lxml


from bs4 import BeautifulSoup
with open('employee.xml','r') as fp:
    data=fp.read()

print(data)
