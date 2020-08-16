try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
    print("pass")           # 에러 회피하기! 어려움을 모른채하지마!! 맞서싸우는거야!!