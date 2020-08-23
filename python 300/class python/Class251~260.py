# # 251


# # 252
# class Human:
#     pass


# # 253
# class Human:
#     pass


# areum = Human()


# # 254
# class Human:
#     def __init__(self):  # 생성자
#         print("응애응애")


# areum = Human()

# # 255


# class Human:
#     def __init__(self, name, age, gender):  # 생성자
#         print("응애응애")
#         self.name = name
#         self.age = age
#         self.gender = gender


# areum = Human("이재윤", "26", "남")
# print(areum.name)


# # 256
# areum.name
# areum.age
# areum.gender


# 257
class Human:
    def __init__(self, name, age, gender):  # 생성자
        print("응애응애")
        self.name = name
        self.age = age
        self.gender = gender

    def selfInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(self.name)
        print(self.age)
        print(self.gender)

    def __del__(self):
        print("나의 죽음을 적에게 알리지 말라")        

areum = Human(name="이재윤", age="26", gender="남성")
areum.who()


# 258
areum.selfInfo(name="김재윤", age="26", gender="남성")
areum.who()


# 259
del areum


# 260
class OMG : 
    def print() : # self (parameter 부재)
        print("Oh my god")

my = OMG()
my.print()