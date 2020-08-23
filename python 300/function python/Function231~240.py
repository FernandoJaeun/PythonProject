# 231
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)  # 에러 변수의 범위 오류

# 232
def makeURL(str):
    return "www." + str + ".com"
print(makeURL("naver"))

# 233
def makeList(str):
    return list(str)
print(makeList("Asdasd"))

# 234
def pickup_even(lst):
    sub = []
    for i in lst:
        if i % 2 ==0:
            sub.append(i)
    return sub
pickup_even([3, 4, 5, 6, 7, 8])

# 235
def convert_int(str):
    myInteger = str.split(".")[0]
    return int(myInteger)

convert_int("123.123")

def convert_int2(str):
    myInteger = int(str.replace(",",""))
    return myInteger
convert_int2("1,234,123")


# 236
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)


# 237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)


# 238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)


# 239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)


# 240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

