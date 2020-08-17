# 파보나치 수 조사

# a = []
# def fabonachi(num):
#     if num > 1:
#         return num * fabonachi(num-1)
#     elif num == 1:
#         return num

# print(fabonachi(6))
# print(a)

result = [1]
limit = 1000

def fibonachi(num):
    for i in range(num):
        if len(result) <= 2:  
            result.append(result[i]+1)
        elif len(result) > 2 and result[i] < limit: # 제한 수치 보다 낮을 때만 값을 추가
            result.append(result[i]+result[i-1])
        else:
            print("이미 허용치를 초과하였습니다. 마지막 수 : %s" % result[-1])
            break

    
def getAddedEven(result):
    a = 0
    for i in result:
        if i % 2 == 0:
            a += i
    return a


fibonachi(50)

print("짝수 값의 합은 : %s" % getAddedEven(result))
