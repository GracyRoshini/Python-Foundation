#--protected varibale : single underscore

class Student:
    def __init__(self,sname,sage):
        self._sname=sname    #--Protected variable
        self._age=sage    #--Protected variable
        self.__studid=2    #--private

    def _disp(self):    #--Protected method
        print('Name: ',self._sname, 'age: ',self._age)


#--derived class
class Marks(Student):
    def __init__(self,sname,sage,mark1):
        super().__init__(sname,sage)     #--Inherit from Student
        self._mark1=mark1    #--Protected variable

    def display_studinfo(self):
        print('Name:',self._sname, 'age:',self._age, 'mark:',self._mark1)


obj=Marks('gracy',21,90)
obj._disp()
obj.display_studinfo()
print(obj._sname)
#print(obj.__studid)  --it is private so not possible will throw error
obj2=Student("a",2)
#print(obj2.__studid)    --it is private so not possible will throw error
