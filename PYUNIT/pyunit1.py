import unittest

def add(a,b):
    return a+b

c=add(2,3)
print(c)


#--Apply Pyunit
class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(10,20),40)    #--adds 10,20 and checks with 40, 30!=40

    def test_add_negative(self):
        self.assertEqual(add(-5,-4),-9)    # -9==-9

    def test_add_mixed(self):
        self.assertEqual(add(-5,2),3)    # -3!=3

    def test_add_mixed_none(self):
        self.assertEqual(add(-5,0),-5)   # -5==-5

unittest.main()    #--built in function
