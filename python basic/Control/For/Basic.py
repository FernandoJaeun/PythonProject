lsitA = [1, 2, 3, 4, 5]

for a in lsitA: #listA의 변수가 a 에 차례대로 담긴다. 즉 listA[0] 부터 listA[마지막] listA[0:] 를 a에 담는다!
    print(a)

listB = [(1,2),(3,4),(5,6)]

for first, last in listB:
    print("%d + %d = %d" % (first, last, first + last)) # 하면서 알았네;; 포매팅은 한 번에 한 %로 끝내야하구나