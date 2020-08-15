file = open("C:/Users/leeja/WorkSpace/Python/Python Project/newFile.txt", 'r') # 파일 내용을 모두 출력하는 방법 1
while True:
    line = file.readline()
    if not line : break
    print(line)
file.close()


file = open("C:/Users/leeja/WorkSpace/Python/Python Project/newFile.txt", 'r') # 파일 내용을 모두 출력하는 방법 2
lines = file.readlines()
for line in lines:
    print(line)
file.close()


file = open("C:/Users/leeja/WorkSpace/Python/Python Project/newFile.txt", 'r') # 파일 내용을 모두 출력하는 방법 3   개취
data = file.read()
print(data)
file.close()
