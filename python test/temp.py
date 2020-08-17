def positive(x):
    return x>0

print(list(filter(positive,[1,4,-1,0,-2,5,7])))

print(sorted(list(filter(lambda x: x>0,[1,4,-1,3,0,-2,5,7]))))
