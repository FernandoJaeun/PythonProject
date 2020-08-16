from mod1 import add    # mod1이란 모듈에서 add라는 메소드만 불러올 때
# from mod1 import add,sub
# from mod1 import *
print(add(1,3))
print(sub(1,4))     # NameError: name 'sub' is not defined
