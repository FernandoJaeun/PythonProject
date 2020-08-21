# 091 딕셔너리 생성
inventory = {'merona': [300, 20],
             'vivivic': [400, 3],
             'sharkbar': {250, 100}}
print(inventory)


# 092 딕셔너리 인덱싱
inventory = {'merona': [300, 20],
             'vivivic': [400, 3],
             'sharkbar': {250, 100}}
print(f"{inventory['merona'][0]} 원")
print(inventory['merona'][0], "원")


# 093 딕셔너리 인덱성
inventory = {'merona': [300, 20],
             'vivivic': [400, 3],
             'sharkbar': {250, 100}}
print(inventory['merona'][1], "개")

# 094 딕셔너리 추가
inventory['worldcorn'] = [500, 7]
print(inventory)


# 095 딕셔너리 keys() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_keylist = list(icecream.keys())
print(icecream_keylist)


# 096 딕셔너리 values() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_price = list(icecream.values())
print(icecream_price)


# 097 딕셔너리 values() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
sum(icecream.values())  # 풀이


# 098 딕셔너리 update 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)


# 099 zip과 dict        Good
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)


# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)