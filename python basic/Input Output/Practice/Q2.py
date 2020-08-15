# 다음 코드가 정상작동하지 않는 원인을 찾고, 정상적인 코드를 작성하시오 close 추가함

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
data = f2.read()
print(data)
f2.close()