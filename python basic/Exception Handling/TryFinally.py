file = open("temp.txt", 'w')
try:
    file.write("new String\n")
finally:    # 주로, 닫아야할 파일이 있을 때 쓴다
    file.close()
