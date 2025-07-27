import unittest

class employee:
    def __init__(self,empid,empname):
        self.empid=empid
        self.empname=empname

    def display(self):
        print('EmpID: ',self.empid)
        print('EmpName: ',self.empname)


obj1=employee(1,'abc')
obj2=employee(2,'def')
obj1.display()
obj2.display()
obj3=obj1

#Apply Pyunit
class TestClass(unittest.TestCase):
    def test_obj(self):
        self.assertIs(obj1,obj3)    #--considered as a testcase

    def test_objNot(self):
        self.assertIsNot(obj1,obj2)

    def test_obj1(self):
        self.assertIs(obj1,obj2)

unittest.main()
