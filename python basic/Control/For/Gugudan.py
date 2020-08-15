a = range(1,10)
b = range(1,10)

for front in a:
    for back in b:
        print("%dx%d=%d " %(front , back, front*back) , end=" ")    # end는 다음 줄로 넘어가지 않고 계속 이어가게 해주는 매개변수당
    print("")