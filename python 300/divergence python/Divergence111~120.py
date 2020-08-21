# # 111 입력받은 내용을 두 번 출력
# print(input("입력하세요 :" )*2)

# # 112
# num = int(input("숫자 : "))
# print(num + 10)

# # 113
# num = int(input("숫자 : "))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# # 114
# num = int(input("숫자 : ")) + 20
# if num < 255:
#     print(num)
# else:
#     print(255)

# # 115
# num = int(input("숫자 : ")) - 20
# if num < 0:
#     print(0)
# elif num > 255:
#     print(255)
# else:
#     print(num)

# # 116
# user = input("현재시간: ")
# if user[-2:] == "00":
#     print("정각")
# else:
#     print("비정각")

# # 117
# fruit = ["사과", "포도", "홍시"]
# user = input("골라 과일 : ")
# if user in fruit:
#     print("줄게")
# else: 
#     print("안줄게")

# # 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = input("투자 종목 선택: ")
# if user in warn_investment_list:
#     print("몰빵")
# else :
#     print("후퇴")


# # 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("계절 : ")
# if user in list(fruit.keys()):
#     print("나도")
# else:
#     print("조흐아?")

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("계절별 과일 : ")

if user in list(fruit.values()) :
    print("나도")
else:
    print("조흐아?")

