# 별 표현식 feat. star expression
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

# 081 star expression
score = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score =  score[:2],score[2:]
print(a)
print(valid_score)


# 082
score1 = score[0:2]
score2 = score[0:-8:-1]
print(score2)
