class MyError(Exception): # 기본적으로 Exception 이라는 내장 클래스를 상속받아야한다!
    pass

def say_nick(nick):
    if nick == "바보":
        raise MyError() # 에러 발생시키는 곳
    print(nick)


try:
    say_nick("cjstk")
    say_nick("바보")
except MyError: # 이 에러가 발생한다면,
    print("바보아니야!")
