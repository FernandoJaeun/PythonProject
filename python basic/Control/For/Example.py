marks = [50,60,80,70,75,90]
number = 0
for mark in marks:
    number += 1
    if(mark > 60):
        print("%d번째 학생은 합격 입니다. 점수 : %d"  % (number, mark))
    else:
        print("%d번째 학생은 불합격 입니다. 점수 : %d" % (number, mark))