
# 051 리스트 생성
movie_rank = ['닥터스트레인지','스플릿','럭키']


# 052 리스트에 원소 추가
movie_rank.append('배트맨')
print(movie_rank)


# 053 
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

# 054 055 리스트에서 요소 삭제
algo = movie_rank.pop(2)    # 빼와서 리턴
movie_rank.pop(-1)
print(movie_rank)
del movie_rank[2]   # 아예 삭제
del movie_rank[-1]


# 056 리스트 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 057 최솟값 최댓값 찾기
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"max: {max(nums)}")
print(f"min: {min(nums)}")


# 058 리스트 합 출력
nums = [1, 2, 3, 4, 5]
add = 0
for i in nums:
    add += i
print(add)
print(sum(nums))

# 059 리스트 합 출력
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
len(cook)


# 060 리스트의 평균 출력
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))