# Life is too short
# you need java 라는 텍스트가 적힌 파일이 있다. Java를 Python으로 바꿔보자

context = """Life is too short
you need java"""

datas = ""

readFile = open("test2.txt", 'r')
datas = readFile.read()
print(datas)
readFile.close()

writeFile = open("test2.txt", 'w')
for data in datas.split():
    if data == "java":
        writeFile.write(datas.replace("java","Python"))
writeFile.close()