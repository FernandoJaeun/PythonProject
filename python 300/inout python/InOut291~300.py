# # 291
# file = open('C:/Users/leeja/OneDrive/바탕 화면/매수종목1.txt','w')
# file.write(""" 
# 005930
# 005380
# 035420
# """)
# file.close()

# # 292
# file = open('C:/Users/leeja/OneDrive/바탕 화면/매수종목2.txt','w')
# file.write(""" 
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER
# """)
# file.close()

# # 293
# file = open('C:/Users/leeja/OneDrive/바탕 화면/매수종목.csv','w',encoding='cp949')
# file.write(""" 
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER
# """)
# file.close()

# # 294
# lst1 = []
# file = open('C:/Users/leeja/OneDrive/바탕 화면/매수종목2.txt','r')
# lst1 = file.read()
# lst1 = lst1.strip()
# print(lst1)
# file.close()


# # 295
# dic1 = {}
# file = open('C:/Users/leeja/OneDrive/바탕 화면/매수종목2.txt')
# lines = file.readlines()
# for line in lines:
#     line = line.strip()
#     k,v = line.split()
#     dic1[k] = v
# print(dic1)


# # 296
# per = ["10.31", "", "8.00"]
# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)

# 297
per = ["10.31", "", "8.00"]
per_int = []
for i in per:
    try:
        per_int.append(int(float((i))))
    except:
        per_int.append(int(0))
print(per_int)


# 298
for i in range(0,5):
    try:
        print(3 / i)
    except(ZeroDivisionError):
        print("제로")

# 299
data = [1,2,3]
for i in range(5):
    try:
        print(data[i])
    except(IndexError) as iderr:
        print(iderr)

# 300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
