file = open("C:/Users/leeja/WorkSpace/Python/Python Project/with.txt", 'w')
file.write("Life is too short, you need python")
file.close()           # 항상 .close()를 실행 시키는게 귀찮은 사람 주목!


with open("C:/Users/leeja/WorkSpace/Python/Python Project/with.txt", "w") as file: # with문을 쓰게 되면 이 안을 벗어나는 순간 자동으로 close() 시키기 때문에 간편하다!
    file.write("Life is too short, you need python")

    