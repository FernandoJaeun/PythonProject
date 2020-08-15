a = [1, 2, 3, 4]
result = []

for v in a:
    result.append(v*3)

print(result)

a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)


b = [2,3,4,5,6,7]
result = [num *3 for num in b if num%2==0]    # 완전 영어식!! 대박!!
print(result)