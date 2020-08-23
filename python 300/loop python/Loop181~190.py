# # 181
# apart = [[101, 102], [201, 202], [301, 302]]
# print(apart)

# # 182
# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
# print(stock)

# # 183
# stock = {'시가': [100, 200, 300], '종가': [80, 210, 330]}
# print(stock)

# # 184
# stock = {'10/10': [80, 110, 70, 90], '10/11': [210, 230, 190, 200]}
# print(stock)

# # 185
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     print(i[0])
#     print(i[1])
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j)

# # 186
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in range(len(apart),0,-1):
#     for col in apart[row-1]:
#         print(col)
    
# for row in apart[::-1]:
#     for col in row:
#         print(col)


# # 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for col in row[::-1]:
#         print(col)

# # 188
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
#         print("---------------")

# # 189
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
#     print("---------------")


# 190
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
print("---------------")
