#--BREAK

str1 = "computer"

for i in str1:
    print(i)
    if i== 'p':
        break

print('completed')

#--------------

#--continue
sum = 0
i = 1

while i<=5:
    num=int(input("enter num:"))
    if num<0:
        print('Negative value')
        continue
    else:
        sum=sum+num
    i=i+1

print('sum',sum)
