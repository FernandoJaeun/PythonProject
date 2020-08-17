class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if(self.value >= 100):
            print("100 이상을 가질 수 없습니다/" ,end ='  ')
            print("초과값 : %s" %(self.value - 100))
            self.value = 100

cal = MaxLimitCalculator()

cal.add(10)
cal.add(50)
cal.add(70)

print(cal.value)

