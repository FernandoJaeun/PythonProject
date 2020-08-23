# # 241
# import datetime
# now = datetime.datetime.now()
# print(now)

# # 242
# print(type(now))


# # 243
# import datetime
# now = datetime.datetime.now()
# for day in range(5,0,-1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)


# # 244
# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))

# # 245
# import datetime

# day = "2020-08-17"
# fday = datetime.datetime.strptime(day,"%Y-%m-%d")
# print(fday)

# # 246
# import time
# import datetime

# while True:
#     print(datetime.datetime.now())
#     time.sleep(1)


# # 247
# import abc
# from something import abc 

# import abc as qwe
# from something import abc  as qwe


# # 248
# import os
# print(os.getcwd())


# # 249
# from os import rename as rename1
# path = "C:/Users/leeja/OneDrive/바탕 화면/"
# newName = "test123.txt"

# rename1(path + "temp.txt" ,path + newName)

# 250
import numpy

for i in numpy.arange(0.0,5.0,0.1):
    print(round(i,1), end=" ")

