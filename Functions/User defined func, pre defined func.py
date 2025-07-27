#Function

"""1) User define function 2) Pre-defined functions (eg: print, input, sort, reverse)
USER DEFINED FUNCTIONS:
1) Function with parameters with returned value
2) Function with parameter without return value
3) Function without parameter with return value
4) Function without parameter without return value
"""

#--Function with parameter with return value
def fun_return_add(a,b):
    c=a+b
    return c

res=fun_return_add(2,3)
print("Addition Result: ",res)

#--Function without parameter with return value
def fun_sub():
    a=10
    b=5
    c=a-b
    return c

res1= fun_sub()
print("Subtraction Result: ", res1)

#--Function with parameter without return value
def fun_mul(a,b):
    c=a*b
    print("Multiplication Result: ",c)

fun_mul(2,4)

#--Function without parameter without return value
def fun_div():
    a=10
    b=5
    c=a/b
    print("Division Result: ",c)

fun_div()
    
