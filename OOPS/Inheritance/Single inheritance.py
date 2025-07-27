#--Single inheritance

#Base class
class base_person:
    def __init__(self,name):
        self.name=name
        print("base class constructor")
        
    def display_parent(self):
        print("base class func",self.name)

#Derived class
class derived_child(base_person):
    def add(self,a,b):
        print('Derived func')
        c=a+b
        return c


obj=derived_child("abc")
obj.display_parent()  #--call base class fun
res=obj.add(2,3) #--derived class
print("add: ",res)

#obj2=base_person()
#obj2.display_parent()
