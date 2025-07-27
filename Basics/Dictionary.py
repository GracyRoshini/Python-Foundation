#--Dictionary

dict={'e1':'A', 'e2':'B', 'e3':'C'}

print(dict)
print(dict.items())
print(dict.keys())
print(dict.values())

#get
print(dict.get('e2'))

#check key
if 'e3' in dict:
    print('e3 is present')

#update
dict.update({'e2':'happy'})
print('After modification of dictionary: ',dict)

#remove pop
dict.pop('e2')
print('After POP of dictionary: ',dict)

#pop item
dict.popitem()
print('After POPitem of dict: ',dict)

#add element
dict['e5']='d'
print('After adding value: ',dict)
