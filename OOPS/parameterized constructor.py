#--parameterized constructor

class Student:
    def __init__(self,name,age):  #--parameterized constructor
        self.name=name #--similiar to 'this' keyword in Java, here 'self'
        self.age=age
        print('name: ',self.name)
        print('age: ',self.age)

    def display_student(self,rollno):
        print('name: ',self.name)
        print('age: ',self.age)
        print('roll no: ',rollno)


obj1=Student("Abc",20)
obj2=Student("Vijay",21)

obj1.display_student(1)
obj2.display_student(2)
