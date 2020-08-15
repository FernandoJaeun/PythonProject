# 다음과 같은 프로그램을 작성하세요  while문 사용
# *
# **
# ***
# ****
# *****

star = '*'
size = 5
weight = 0
while size > 0:
    weight += 1
    temp = weight
    while temp > 0:
        print(star, end='')
        temp -= 1
    print('')
    size -= 1
