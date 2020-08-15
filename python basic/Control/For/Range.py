marks = [90, 60, 80, 70, 75]

for number in range(len(marks)):
    if(marks[number]<60):
        continue
    else:
        print("%d번째 학생의 점수는 %d입니다. 합격" %(number+1 , marks[number]))

