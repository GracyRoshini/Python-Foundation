#--Multi level

class base1:
    def add(self,a,b):
        c=a+b
        return c
 
class derived1(base1):
    def sub(self,a,b):
        c=a-b
        return c

class derived2(derived1):
    def mul(self,a,b):
        c=a*b
        return c


obj=derived2()
r1=obj.add(2,3)
r2=obj.sub(4,2)
r3=obj.mul(2,3)
print("base class1 function add: ",r1)
print("Derived class1 function sub: ",r2)
print("Derived class2 func mul: ",r3)

        
