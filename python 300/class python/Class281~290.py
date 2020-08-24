# 281
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def carInfo(self):
        print("차 정보")
        print(f"바퀴 수 : {self.wheel}")
        print(f"가격 대 : {self.price}")

# 282
class Bike(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)
    def carInfo(self):
        print("자전거 정보")


# 283
me = Bike(2, 100)
me.carInfo()
print(me.wheel)
print(me.price)

# 284


class AutoMove(Car):
    def __init__(self, wheel, price, brand):
        self.wheel = wheel
        self.price = price
        self.brand = brand

    def Info(self):
        print("자전차 정보")
        print(self.wheel)
        print(self.price)
        print(self.brand)

me2 = AutoMove(2, 100, "시마노")
me2.Info()

# 285
morning = Car(4, 12000)


# 286




# 287


# 288


# 289


# 290
