# 사용자의 입력을 받는 파일을 만들어보자. test.txt를 사용, 기존 내용이 유지되고 값이 추가되도록

file = open("test.txt" , 'a')
file.write("\nnew String")
file.close()