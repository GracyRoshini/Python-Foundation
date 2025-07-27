#--Arithmetic Operators
x=10
y=3

add = x+y
sub = x-y
mul = x*y
div = x/y

exp = x**y
mod = x%y
floor_div = x//y

print('add:', add)
print('sub:',sub)
print('mul:',mul) 
print('div:',div)

print('exponent of x with y:', exp)
print('modulo:', mod)
print('Floor division:', floor_div)

#--Formats
price =100.56
item='jeans'
qty=5

order='order items: {} of quantity: {} with price: {}'
print(order.format(item,qty,price))

#--index with format
order= "order item: {2} of quantity: {0} with price: {1}"
print(order.format(item,qty,price))

#--named index format
order ="order item: {a} of qty: {b} with price :{c}"
print(order.format(a="mobile", b=9, c=20000))

#---------------------------------------------------------------------------------------------
#--User Input:input
#--Output: print

#a=input("Enter a:") #5
#b=input("Enter b:") #3

c=a+b 

print(c)#--5 3

#------------
#name=input('Enter employee')
#age=int(input('Enter age of employee'))

#basic_salary = int(input("enter basic salary:"))
#hra=int(input("Enter hra"))

#total_salary=basic_salary+hra

print("employee name:",name)
print("employee age:",age)
print("basic sal:", basic_salary)
print("employee hra:", hra)
print("employee total sal:",total_salary)

#---------------------------
#--IF
a=15
b=35

if(a>b):
    print("a is greater than b",a)
else:
    print("B is greater than a",b)

#--Nested IF
a=24
b=4
c=66

if a>b:
    if a>c:
        print("A is greater")
    else:
        print("C is greater")
else:
    if b>c:
        print("B is greater")
    else:
        print("C is greater")


































