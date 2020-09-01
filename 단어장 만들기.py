with open(file="C:/Users/leeja/WorkSpace/Python/Python Project/sub/vocaulary.txt",
          mode='a',
          encoding='utf-8') as file:
    while True:
        context = input("영어 단어를 입력하세요: ")
        if context == "q":
            break
        file.write(context + "\n")

        context = input("한국어 뜻을 입력하세요: ")
        if context == "q":
            break
        file.write(context + "\n")

        print("")
