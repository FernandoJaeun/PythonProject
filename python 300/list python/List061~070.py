# 061 숫자만 출력해라
price = ['20180728', 100, 130, 140, 150, 160, 170]
price[1:]


# 062 슬라이싱을 이용해서 홀수만 빼내라
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums[::2]

# 063 슬라이싱을 이용해서 짝수만 빼내라
print(nums[::-2])   # 나
print(nums[1::2])   # 정답

# 064 슬라이싱을 써서 숫자를 역방향 출려ㅑㄱ
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::-1])

# 065 
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0::2])   # 나
print(interest[0], interest[2])   # 정답


# 066 join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
for i in interest:
    print(i,end=" ")    # 나
print(" ".join(interest))   # 정답

# 067
print("/".join(interest))

# 068
print("\n".join(interest))


# 069 문자열 split 메서드
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)


# 070 리스트 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)

