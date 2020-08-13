a = "hobby"

a.count("b")
a.find("y") # 있으면 문자의 위치 int 반환
a.find("b")
a.find("q") # 없으면 -1 반환 

a.index("b") # 있으면 문자의 위차 int 반환
a.index("ㅂ") # 없으면 error 반환

b = ["이재윤" , "도상훈" , "이용수" , "최서윤",["신현규","김일중","이창희"]]
c = [1 , 2 , "dlwodbs"]
c[0:0] = [5, 2] # 0부터 0 자리에 [5,2]를 넣다(바꾸다)
print(b[0])
print(b[1])
print(b[2])
print(b[4][0])  # Json 이랑 비슷하네
print(c)

q = [1, 2, 3]
w = [4, 5, 6]
print(q+w)

print(b[0:3])     # list slicing!
print(b*3)