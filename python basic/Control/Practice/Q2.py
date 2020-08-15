# 1부터 1000까지의 자연수 중 3의 배수의 합은? while문 사용

a = 0
add = 0
while a < 1000:
    a += 1
    if(a % 3 == 0):
        add += a
print(add)
