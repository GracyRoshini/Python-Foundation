#Function keyword

def employee(eid,ename):
    print('eid', eid)
    print('ename',ename)

employee(eid = 'e1', ename = 'vino')

#Function keyword with *args(keyword) --can only pass values
def marks(*args):
    print(args)

marks(10,20,30)

#Function keyword with **args(keyword) --can pass values along with parameters
def marks_keywordArgs(**args):
    print(args)

marks_keywordArgs(id=1, name='vino', age=29)
