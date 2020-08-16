class FourCalculator:
    def __init__(self, first, second):    # 객체의 인스턴스가 생성될 때 실행되는 메소드로써 생성자라고 말한다!
        self.first = first                # 인스턴스가 초기화 될 때 매개변수를 받아 할당할 수 있다
        self.second = second

    def setData(self, first, second):
        self.first = first        # self.first --> 객체 변수!!
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


a = FourCalculator(5,1)
a.add()
a.div()


# 상속(Inheritance)
class MoreFourCal(FourCalculator):  # FourCalculator 클래스의 생성자 부분을 상속받았다
    def pow(self):                # 그리고 제곱이라는 기능을 덧붙여 쓰고 있다 대박!
        return self.first ** self.second    # a ** b --> a의 b 제곱

b = MoreFourCal(5,5)
b.pow()

# 메소드 오버라이딩(Overriding) : 자식의 메소드로 부모의 메소드를 덮어씀. 메소드 명이 같아야함!
class SafeFourCalc(FourCalculator):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return FourCalculator.div(self)
c = SafeFourCalc(4,3)
c.div()
print(c.div())