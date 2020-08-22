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


# 125
num_list = {'011' :'SKT', 
            '016' :'KT' , 
            '019' :'LGU', 
            '010' : '알수없음' }
user = input("number = ")
user_phone = user.split("-")[0]
if user_phone in list(num_list.keys()):
    print(f"당신은 {num_list[user_phone]} 사용자 입니다")
else :
    print("니 누꼬?")

 
# 126
# 127
# 128
# 129
# 130
