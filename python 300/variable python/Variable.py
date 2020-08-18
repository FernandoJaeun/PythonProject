# 011 ~ 012 변수 사용하기
samsung = 50000
print(samsung * 10)

marketCap = 298 * 1000000 * 10000000
presentValue = 50000
PER = 15.79
print(marketCap, type(marketCap))
print(presentValue, type(presentValue))
print(PER, type(PER))

# 013 문자열 출력
s = "hello"
t = "python"
print(s, t, sep="! ")
print(s + "!" + t)

# 014 파이썬을 이용한 값 계산
print(2 + 2 * 3)

# 015 type 함수
a = 128
print(type(a))
a = "128"
print(type(a))


# 016 문자열을 정수로 변환
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int)) # 숫자 확인용 +1


# 017 정수를 문자열 100으로 변환
num_int = 100
num_str = str(num_int)
print(num_str + "!", type(num_str))


# 018 문자열을 실수로 변환
num_str ="15.79"
num_float = float(num_str)
print(num_float, type(num_float))


# 019 문자열을 정수로 변환
year = '2020'
year_int = int(year)
print(year_int-1 ,year_int-2, year_int-3)

# 020 파이썬 계산
pay_montly = 48584
installment = 36
total = pay_montly * installment
print("할부 총액 : %d" %(total) )