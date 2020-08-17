# 3과 5의 배수 합하기, 1000 미만의 수로

# 3 6 9 12 15 18 ...
# 5 10 15 20 25 ...
numbers = []
for i in range(1, 1001):
    numbers.append(i)

result = 0

for i in numbers:
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)