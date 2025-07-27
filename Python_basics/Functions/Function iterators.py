#--Function Iterator

num=[20,40,10,60,70]

for i in num:
    print(i)

#--Iterator
res=iter(num)

print('---Iter---')
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

