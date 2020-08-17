# 최대 소인수
# 수 600851475143의 가장 큰 소인수는 무엇입니까?


num = 602
div = 1
result = []

while True:
    if num % div == 0:
        result.append(div)
    div += 1
    if num / div < 1:
        break
print(result)

myLargestPrimeNum = []
def getLargestPrimeNumber(number):
    for i in range(1,number+1):
        if number % i == 0 and i == number:
            print(i)  


for i in result:
    getLargestPrimeNumber(i)