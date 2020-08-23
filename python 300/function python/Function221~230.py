# # 221
# def print_reverse(in_str):
#     print(in_str[::-1])
#     for i in in_str[::-1]:
#         print(i, end='')


# print_reverse("asdasqwef")
# # 222


# def print_score(lst):
#     add = 0
#     for i in lst:
#         add += i
#     print(add / len(lst))
#     print(sum(lst)/len(lst))


# print_score([1, 2, 3])


# # 223
# def print_even(lst):
#     new_lst = []
#     for i in lst:
#         if i % 2 == 0:
#             new_lst.append(i)
#     print(new_lst)


# print_even([1, 3, 2, 10, 12, 11, 15])

# # 224


# def print_keys(dic):
#     print(dic.keys())

# print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

# # 225
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}


# 226
def print_5xn(in_str):
    chunk_num = int(len(in_str)/5)
    for x in range(chunk_num+1):
        print(in_str[x*5: x*5 + 5])


print_5xn("qweasdzxcewqdsaczx")


# 227
def print_mxn(string, index):
    chunk_num = int(len(string)/index)
    for x in range(chunk_num + 1):
        print(string[x*index: x*index+3])


print_mxn("아이엠어보이유알어걸", 3)

# 228
def calc_monthly_salary(annual_salary):
    print(int(round(annual_salary/12,-1)))

calc_monthly_salary(1200001)
# 229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

# 230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)