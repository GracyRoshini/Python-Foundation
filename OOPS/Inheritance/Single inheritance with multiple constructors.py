#--Single inheritance

#Base class
class base_person:
    def __init__(self,name):
        self.name=name
        print("base class constructor")
        
    def display_parent(self):
        print("base class func : Employee name: ",self.name)

#Derived class
class derived_child(base_person):
    def __init__(self,name,emp_salary,empid):
        super().__init__(name) #--super keyword used to call the constructor of the base class
        self.emp_salary=emp_salary
        self.empid=empid
        
    def add(self,a,b):
        #print('Derived func')
        c=a+b
        return c

    def display_empinfo(self):
        print('name: ',self.name, 'Id ', self.empid, 'salary: ',self.emp_salary)


obj=derived_child("abc",20000,1)
obj.display_parent()  #--call base class fun
res=obj.add(2,3) #--derived class
print("add: ",res)
obj.display_empinfo()
