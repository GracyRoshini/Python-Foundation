
list1=[10,40,20,60]

list2=list1
print('print list1', list1)
print('print list2', list2)

list2[2] = 80
print('After modifying list1 becomes: ',list1)
print('After list2: ',list2)

#Changes made in list2 is reflected back on list1 also, to avoid this we use (deepcopy) method

print("-------------------")

import copy

list3=[10,20,90,30]
list4=copy.deepcopy(list1)

print('list3: ',list3)
print('list4: ',list4)

list3[2]=100

print("After modification")
print('List3: ',list3)
print('List4: ',list4)
