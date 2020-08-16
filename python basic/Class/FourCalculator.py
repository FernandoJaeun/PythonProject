class FourCalculator:
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


asd, qwe = 3, 5
zxc, cxz = 5, 7

a = FourCalculator()
a.setData(asd, qwe)
print(a.first)
print(a.second)

b = FourCalculator()
b.setData(zxc, cxz)
print(b.first)
print(b.second)

id(a.first)     # 객체의 주소를 돌려주는 내장함수!
id(a.second)

id(b.first)
id(b.second)

a.add()
a.sub()
a.mul()
a.div()

b.add()
b.sub()
b.mul()
b.div()

