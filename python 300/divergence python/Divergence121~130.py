# # 121
# user = input("문자 하나 입력 : ")
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())

# # 122
# score = int(input("점수를 입력 : "))
# if score > 81 and score < 100:
#     print("A")
# elif score > 61 and score < 80:
#     print("B")
# elif score > 41 and score < 60:
#     print("C")
# elif score > 21 and score < 40:
#     print("D")
# else:
#     print("E")


# # 123
# moneys = {'달러' : 1167, '엔' : 1.096, '유로' : 1268 , '위안' : 171}
# #user = input("얼마 어떤 : ").split(" ")
# # won = int(user[0])
# # unit = user[1]
# user = input("얼마 어떤 : ")
# won, unit = user.split()

# if unit in list(moneys.keys()):
#     print(int(won) * moneys[unit])


# # 124
# num_list = []
# num_list.append(int(input("input num 1 : ")))
# num_list.append(int(input("input num 2 : ")))
# num_list.append(int(input("input num 3 : ")))
# print(num_list)
# print(max(num_list))


# # 125
# num_list = {'011': 'SKT',
#             '016': 'KT',
#             '019': 'LGU',
#             '010': '알수없음'}
# user = input("number = ")
# user_phone = user.split("-")[0]
# if user_phone in list(num_list.keys()):
#     print(f"당신은 {num_list[user_phone]} 사용자 입니다")
# else:
#     print("니 누꼬?")


# # 126
# gus = ['강북구', '강북구', '강북구',
#        '도봉구', '도봉구', '도봉구',
#        '노원구', '노원구', '노원구', '노원구']
# nums = [0, 1, 2,
#         3, 4, 5,
#         6, 7, 8, 9]
# zipcode = dict(zip(nums, gus))

# user = list(input("우편번호를 입력 : "))
# user_zip = int(user[2])

# if user_zip in nums:
#     print(zipcode[user_zip])


# # 127
# RRnum = input("당신 주민 번호 입력 : ")
# gender = RRnum.split("-")[1]
# gender = gender[0]
# print(gender)
# if gender == ('1' or '3'):
#     print("성별은 남성")
# else:
#     print("성별은 여성")

# # 128
# RRnum = input("당신 주민 번호 입력 : ")
# region = RRnum.split("-")[1][1:3]
# seoul = ['00','01','02','03','04','05','06','07','08']
# if region in seoul :
#     print("출생지는 서울입니다")
# else:
#     print("서울 사람이 아닙니다")


# # 129 sun of beach
# RRnum = input("당신 주민 번호 입력 : ")
# RRnum = RRnum.split("-")
# validation = [[2, 3, 4, 5, 6, 7], [8, 9, 2, 3, 4, 5]]

# 130

import requests
url = "https://api.bithumb.com/public/ticker/"
btc =  requests.get(url).json()['data']
opening_price = btc['opening_price']
closing_price = btc['closing_price']
min_price = btc['min_price']
max_price= btc['max_price']
