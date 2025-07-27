#--LIST

list=['a', 123, 'Abcdefg', 89.3434]

print(list)

for i in list:
    print(i)

print(list[2])

#---------------------------------------------------
#--functions in list

marks=[90,60,50]
print("marks:",marks)

#append
marks.append(100)
print("append:",marks)

#extend
marks.extend([80,70])
print("extend:",marks)

#sort
marks.sort()
print("sort:",marks)

#min and max
print("min:", min(marks)," max: ",max(marks))

#len
print('len:',len(marks))

#count
print('Count: ',marks.count(60))

#reverse
marks.reverse()
print(marks)

#edit/modify
marks[1]=20
print("Modified list: ",marks)

#pop
marks.pop()
print("After removal of item: ",marks)

marks.pop(1)
print("After removal of items in position 1: ",marks)





