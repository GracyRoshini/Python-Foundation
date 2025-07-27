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

#--
name=input()
no_ticketint(input())
age=int(input())
gender=input("Enter gender:")
price=float(input("Enter price:"))

if age<5:
    price=0
elif (age>50 and age<60 and gender == 'f'):
    price=price*0.5
elif age>55 and age<60 and gender=='m':
    price=price*0.5
elif age>=60:
    price=price*0.3
else:
    price=price

print("name:",name)
print("no of tickets:", tickets)
print("age:", age)
print("gender:", gender)
print("price:",price)



