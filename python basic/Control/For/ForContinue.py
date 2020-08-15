marks = [60, 40, 80, 50, 90, 70]
number = 0

for mark in marks:
    number += 1
    if(mark < 60):
        continue
    print("%d번쨰 학생은 합격 입니다. 점수 : %d" % (number, mark))
