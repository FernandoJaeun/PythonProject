a = range(1, 101)
for num in a:
    if num > 9:
        print(num, end=' ')
    else:
        print(" %d" % num, end=' ')
    if(num % 10 == 0):
        print("")
