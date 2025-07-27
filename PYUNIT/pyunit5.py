import unittest

obj1=[10,20]
obj2=[10,20]
obj3=obj1
obj4=None

#Apply pyunit
class Test(unittest.TestCase):
    def test_instance(self):
        self.assertIs(obj1,obj3)
        #self.assertIs(obj1,obj2)

    def test_NotInstance(self):
        self.assertIsNot(obj1,obj2)

    def test_none(self):
        self.assertIsNone(obj4)
        self.assertIs(obj4,None)
        


unittest.main()
