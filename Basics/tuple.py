#--tuple
name=('raj', 90, 78,(10,20))

for i in name:
    print(i)

print('name[3]: ',name[3])
print('name[3][0]: ',name[3][0])
print('name[3][1]: ',name[3][1])

#--TUPLES ARE IMMUTABLE NOT CHANGEABLE
#--CONCAT +
mark=(20,60,90)
new_tuple=name+mark
print("new tuple: ",new_tuple)

#--multiply *
print('multiply: ',mark*3)

#--check
if 60 in mark:
    print('60 present')
