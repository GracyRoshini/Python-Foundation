#--Lambda: Asynchronous functions: map, filter, reduce
#Using non-block code: db operation, file operations, queries
#Lambda: take multiple args to the expression and return single value

res=lambda a:a*10
print(res(5))

mul=lambda a,b,c : a*b*c
print(mul(2,5,6))

#map
sal=[10000,20025,45000,60000]
inc_sal=list (map (lambda x:x+1000,sal))
print("Incremented map salary: ",inc_sal)

#Filter
res_filter = list(filter(lambda x:(x%2==0),sal))
print("filter result: ",res_filter)

#reduce  --it used a specific package called reduce import from functools
from functools import reduce

res_reduce = reduce(lambda x,y:x+y, sal)
print("reduce result: ",res_reduce)


max_reduce= reduce(lambda x, y:x if x>y else y, sal)
print('Max salary: ', max_reduce)

#-------------------------------------------------------------------
print("----------------------------------------------------")

def get_input():
    n=int(input("enter no of tickets: "))
    tickets =[]
    for i in range(n):
        print("ticket:", i+1)
        name=input("enter name: ")
        age=int(input("enter age: "))
        gender=input("enter gender (M/F): ")
        price=float(input("enter ticket price: "))
        tickets.append({'name' : name, 'age':age, 'gender':gender, 'price':price}) #--creating dict and passing it to list using append
    return tickets

def calculate(tickets):
    for t in tickets:
        if t['age']>60 or t['age']<5: #--t is a dictionary, age is key
            t['price'] *= 0.5
    return tickets

def display1(tickets):
    print("\n--Ticket details--")
    for t in tickets:
        print(f"Name: {t['name']}, Age: {t['age']}, Gender: {t['gender']}, Final Price: {t['price']}") #--using format for{}

def display2(tickets):
    age1=map(lambda t:t['age'], tickets)
    max_age= reduce(lambda x, y:x if x>y else y, age1)
    print(f"\nMax age among passengers: {max_age}")

    updated_ages=list(map(lambda t:t['age']+2, tickets))
    print("Ages incremented by 2: ", updated_ages)
    

tickets=get_input()
tickets= calculate(tickets)
display1(tickets)
display2(tickets)



