# # 191
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# tax = 0.00014
# for row in data:
#     for col in row:
#         print(col + (tax * col))
#     #   print(col * 1.00014)

# # 192
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# tax = 0.00014
# for row in data:
#     for col in row:
#         print(col * 1.00014)
#     print("----------")


# # 193
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# tax = 0.00014
# result = []
# for row in data:
#     for col in row:
#         result.append((col * 1.00014))
# print(result)

# # 194
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# tax = 0.00014
# result = []
# for row in data:
#     sub = []
#     for col in row:
#         sub.append((col * 1.00014))
#     result.append(sub)
# print(result)


# # 195
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     for j in i[-1:]:
#         print(j)
# for i in ohlc[1:]:
#     print(i[-1])


# # 196
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#     if row[-1] > 150:
#         print(row[-1])

# # 197
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#     if row[-1] >= row[0]:
#         print(row[-1])


# # 198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for row in ohlc[1:]:
#     volatility.append((row[1] - row[2]))
# print(volatility)


# # 199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for row in ohlc[1:]:
#     if row[-1] > row[0]:
#          print(row[1] - row[2])


# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
result = 0
for row in ohlc[1:]:
    result += (row[0] - row[-1])
print(result)