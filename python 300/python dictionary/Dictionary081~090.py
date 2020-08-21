# 별 표현식 feat. star expression
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

# 081 star expression
score = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score = score[:2], score[2:]
print(a)
print(valid_score)

# 082
score1 = score[0:2]
score2 = score[0:-8:-1]
print(score2)

# 083
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score = scores[0:1],scores[1:9]
print(valid_score)  # 나

a, *valid_score, b, c = scores  
print(valid_score)  # 풀이  


# 084 비어있는 딕셔너리
temp = {}


# 085   딕셔너리 요소 생성
icecream = {'merona': 1000, 'polarpo' : 1200, 'bbangbbare' : 1800}
print(icecream)

# 086   icecream 에 제품 추가
icecream.update({'sharkbar':1200, 'worldcorn':1500}) # 나
print(icecream) 
icecream['sharkbar'] = 1200 # 풀이
icecream['worldcorn'] = 1500


# 087   Value 출력
print(f" 메로나 가격 : {icecream['merona']}")


# 088    값 수정
icecream['merona'] = 1300
print(icecream) 

# 089   값 삭제
del icecream['merona']
print(icecream) 

# 090   에러 이유
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000} 
icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
