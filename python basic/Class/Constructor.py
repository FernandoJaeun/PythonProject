class FourCalculator:
    def __init__(caller, first, second):    # 객체의 인스턴스가 생성될 때 실행되는 메소드로써 생성자라고 말한다!
        caller.first = first                # 인스턴스가 초기화 될 때 매개변수를 받아 할당할 수 있다
        caller.second = second

    def setData(caller, first, second):
        caller.first = first        # caller.first --> 객체 변수!!
        caller.second = second

    def add(caller):
        return caller.first + caller.second

    def sub(caller):
        return caller.first - caller.second

    def mul(caller):
        return caller.first * caller.second

    def div(caller):
        return caller.first / caller.second


a = FourCalculator(5,1)
a.add()
a.div()


# 상속(Inheritance)
class MoreFourCal(FourCalculator):  # FourCalculator 클래스의 생성자 부분을 상속받았다
    def pow(caller):                # 그리고 제곱이라는 기능을 덧붙여 쓰고 있다 대박!
        return caller.first ** caller.second    # a ** b --> a의 b 제곱

b = MoreFourCal(5,5)
b.pow()

# 메소드 오버라이딩(Overriding) : 자식의 메소드로 부모의 메소드를 덮어씀. 메소드 명이 같아야함!
class SafeFourCalc(FourCalculator):
    def div(caller):
        if caller.second == 0:
            return 0
        else:
            return FourCalculator.div(caller)
c = SafeFourCalc(4,3)
c.div()
print(c.div())