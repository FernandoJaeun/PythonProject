import random


with open(file="C:/Users/leeja/WorkSpace/Python/Python Project/sub/vocaulary.txt",
          mode='r',
          encoding='utf-8') as vocaulary:
    
    contexts = vocaulary.readlines()
    en = contexts[0::2] # cat, dog, tesla, sotck
    ko = contexts[1::2] # 고양이, 개, ...
    while True:
        choiceVoca = random.randint(0,len(en)-1)
        answer = input(ko[choiceVoca].strip()+":")
        if answer == en[choiceVoca].strip():
            print("맞았습니다!")
        elif answer == 'q':
            print("단어장을 종료합니다")
            break
        else:
            print("아쉽습니다", f"정답은 {en[choiceVoca].strip()} 입니다")
        print()

    # for i in range(choiceVoca):
    #     answer = input(ko[i].strip()+":")
    #     if answer == en[i].strip():
    #         print("맞았습니다!")
    #     else:
    #         print("아쉽습니다", f"정답은 {en[i].strip()} 입니다")
    #     print()
