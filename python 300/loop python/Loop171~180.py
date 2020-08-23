# # 171
# price_list = [32100, 32150, 32000, 32500]
# for i in price_list:
#     print(i)

# for i in range(len(price_list)):
#     print(price_list[i])

# # 172
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i, price_list[i])

# for i,v in enumerate(price_list):   # index와 value를 동시에 반환해주는 함수 enumerate
#     print(i,v)

# # 173
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(3-i,price_list[i])

# # 174
# price_list = [32100, 32150, 32000, 32500]
# for i in range(1,len(price_list)):
#     print(90 + (10*i),price_list[i])

# # 175
# my_list = ["가", "나", "다", "라"]
# for i in range(1,len(my_list)):
#     print(my_list[i-1], my_list[i])

# # 176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(2,len(my_list)):
#     print(my_list[i-2], my_list[i-1], my_list[i])

# # 177
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list),1,-1):
#     print(my_list[i-1], my_list[i-2])

# # 178
# my_list = [100, 200, 400, 800]
# for i in range(1,len(my_list)):
#     print(my_list[i] - my_list[i-1])

# # 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(1, len(my_list)-1):
#     print((my_list[i-1] + my_list[i] + my_list[i+1])/3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)