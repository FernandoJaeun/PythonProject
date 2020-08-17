from mod1 import add    # mod1이란 모듈에서 add라는 메소드만 불러올 때
# from mod1 import add,sub
# from mod1 import *
print(add(1,3))
print(sub(1,4))     # NameError: name 'sub' is not defined


a =  [1, -2, 3, -5, 8, -3]

print(list(filter(lambda x : x > 0, a )))

int(0xea)

list(map(lambda x : x*3 , [1,2,3,4]))

a , b = max([-8, 2, 7, 5, -3, 5, 0, 1]) , min([-8, 2, 7, 5, -3, 5, 0, 1])
print(a+b)

round(17/3,4)



print(sys.argv)
import os
os.chdir("C:/Users/leeja/WorkSpace/Python/Python Project/python basic/Module")