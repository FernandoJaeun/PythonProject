# A 학급의 총 10명의 학생이 있다. 다음은 학생들의 중간고사 점수이다.
# A 학급의 평균 점수를 구해보자 for문 사용

classA = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for num in classA:
    total += num

print("평균점수는 %d" % (total/len(classA)))
