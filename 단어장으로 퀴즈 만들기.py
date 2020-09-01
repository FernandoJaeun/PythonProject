with open(file="C:/Users/leeja/WorkSpace/Python/Python Project/sub/vocaulary.txt",
          mode='r',
          encoding='utf-8') as vocaulary:
    contexts = vocaulary.readlines()
    en = contexts[0::2] # cat, dog, tesla, sotck
    ko = contexts[1::2] # 고양이, 개, ...
    for i in range(len(en)):
        answer = input(ko[i].strip()+":")
        if answer == en[i].strip():
            print("맞았습니다!")
        else:
            print("아쉽습니다", f"정답은 {en[i].strip()} 입니다")
        print()
