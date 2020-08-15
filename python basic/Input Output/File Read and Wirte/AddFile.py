file = open("C:/Users/leeja/WorkSpace/Python/Python Project/newFile.txt", 'a') # 새로운 내용을 쓰는 방법!! 매개변수 주목!!!!
for i in range(11,20):
    data = "new %d번쨰 줄입니다.\n" % i
    file.write(data)  
file.close()


file = open("C:/Users/leeja/WorkSpace/Python/Python Project/newFile.txt", 'r') # 파일 내용을 모두 출력하는 방법 3   개취
data = file.read()
print(data)
file.close()
