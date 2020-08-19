# 031 문자열 합치기
a = "3"
id(a)
b = "4"
id(b)
print(a + b)

# 032 문자열 곱하기
a = 'Hi'
id(a)
b = "Hi"
id(b)
a = a * 3
id(a)
print(a)


# 033 문자열 곱하기
string = '-'
print(string * 80)

# 034 문자열 곱하기
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ")*3)


# 035 문자열 출력
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s  나이 : %s" % (name1, age1))
print("이름: %s  나이 : %s" % (name2, age2))


# 036 문자열 출력     # >><<>><<>><<>><<>>>><<>><<>><<>><<>>>><<>><<>><<>><<>>
#format("이름 : " + name1 + " 나이 : " + age1, 15)
print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))


# 037 문자열 출력   f-string          # >><<>><<>><<>><<>>>><<>><<>><<>><<>>>><<>><<>><<>><<>>
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")


# 038 컴마 제거하기
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(",","")
print(int(상장주식수))


# 39 문자열 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
# 분기 = 분기.split("/")
# print(분기[:2])
print(분기[:7])


# 040 strip 메서드
data = "   삼성전자    "
print(data) 
print(data.strip())  # 원래의 공백 삼성전자는 없어지지 않고 다른 메모리에 저장되어 있다. string은 변경할 수 없는 자료형이다