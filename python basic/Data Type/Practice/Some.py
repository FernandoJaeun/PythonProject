a = b = [1,2,3]
a[1] = 4
print(b)
id(a)
id(b)
b is a

a = [1,2,3]
b = a[:]
a[1] = 4
a
b
id(a)
id(b)

from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 4
a
b
id(a)
id(b)
 
a,b =('asd', 'dsa')
a
b

(a,b) = 'asd', 'dsa'
a
b

[a,b] = ['asd','dsa']
a
b

a=b ='asd'
a
b

a,b = b,a