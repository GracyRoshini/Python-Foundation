#polymorphism
class One:
    def add(self,a,b):
       return a+b

class Two(One):
    def add(self,a,b,c):
        return a+b+c

#over riding is same func w same number of parameters in inheritance
#over loading is same func w diff parameters, python does not support this

obj=Two()
print(obj.add(2,3,4)) #--cannot give two parameters to access add(a,b) from class One
#coz python does not support method overloading
#obj.add(2,3)  --won't be supported --overloading not possible

obj2=One()
print(obj2.add(2,3))
