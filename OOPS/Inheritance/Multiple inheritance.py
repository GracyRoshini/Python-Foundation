#--Multiple Inheritance

class base1:
    def add(self,a,b):
        c=a+b
        return c
    
class base2:
    def sub(self,a,b):
        c=a-b
        return c

class base3:
    def mul(self,a,b):
        c=a*b
        return c
 
class derived(base1,base2,base3):
    def div(self,a,b):
        c=a/b
        return c


obj=derived()
r1=obj.add(2,3)
r2=obj.sub(4,2)
r3=obj.mul(2,3)
r4=obj.div(6,2)
print("base class1 function add: ",r1)
print("base class2 function sub: ",r2)
print("base class3 func mul: ",r3)
print("Derived class function : ",r4)

        
