# 261
class Stock:
    def __init__(self, name, code, PER, PBR, DY):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.DY = DY

    def setName(self, name):
        self.name = name

    def setCode(self, code):
        self.code = code

    def setPER(self, PER):
        self.PER = PER

    def setPBR(self, PBR):
        self.PBR = PBR

    def setDY(self, DY):
        self.DY = DY

    def getName(self):
        return self.name

    def getCode(self):
        return self.code


# 262
# samsung = Stock("asdasd", "123123")
# print(samsung.name)
# print(samsung.code)


# # 263
# samsung = Stock(None, None)
# print(samsung.name)
# samsung.setName("samsung")
# print(samsung.name)


# # 264
# samsung.setCode("13512")
# print(samsung.code)


# 265
# print(samsung.getName())
# print(samsung.getCode())

# 266


# 267
stock = Stock("삼성전자", "12345", "10", "15" , 2.5)
print(stock.DY)
# 268


# 269
stock.setPER("22")
print(stock.PER)

# 270
portfolio1 = ("삼성전자","12345","12", "25", 2.1)
portfolio2 = ("현대자동차","23345","22", "26", 1.8)
portfolio3 = ("SK하이닉스","42125","21", "29", 3.9)

