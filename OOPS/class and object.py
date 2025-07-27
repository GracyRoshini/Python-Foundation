#--Class and object

class one:  #--sub class

    company_name='hexaware'  #--global variable
    a=20  #--global variable

    def __init__(self):
        print("Constructor")
    
    def fun1(self):  #--sub function 1
        a=10
        print('Funct 1 is called')
        print('a: ',a)

    def fun2(self,location):  #--local variable , sub function 2
        print('place: ',location)

#--Object
obj1=one()  #--create the obj: declaration, for assigning sub class
obj1.fun1()

obj2=one()
obj2.fun1()
obj2.fun2('banglore')  #--Have to pass arg

print(obj1.company_name)  #Directly accessing variable with object created
print(one.company_name)  #calling with class name

obj1.fun2("Chennai")  #--calling sub function w created object1 and passing arg
obj2.fun2("banglore") #--calling sub function w created object2 and passing arg
