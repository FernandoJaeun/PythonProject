# 071 튜플 생성
my_variable = ()
print(type(my_variable))

# 072 튜플에 값 할당
movie_rank = ("닥터스트렌지", "스플릿", "럭키")


# 073 숫자 1 이 저장된 튜플을 생성
num1 = (1,)
print(type(num1))


# 074 오류 원인 추적
t = (1, 2, 3)
t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# 075 튜플 생성 방법    괄호 하는 게 표준이지만 사용자 편의를 위해 괄호 없이도 동작한다.
t = 1, 2, 3, 4


# 076
# t = ('a', 'b', 'c') --> t = "A", "b","c" 가능?


# 077 튜플을 리스트로 변환
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)


# 078 리스트를 튜플로 변환
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data2 = tuple(interest)
print(data2)


#079 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)


# 080 range 함수
tuple1 = tuple(range(2,100,2))
print(tuple1)