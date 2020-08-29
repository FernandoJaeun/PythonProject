import sys, os

folderPath = "C:/Users/leeja/OneDrive/바탕 화면/하루일기/2020/8/"
fileNames = os.listdir(folderPath)
i = 28

for name in fileNames:
    try:    
        if name.find("복사본") is not -1:
            src = os.path.join(folderPath, name)
            dst = str(i) + '.txt'
            dst = os.path.join(folderPath, dst)
            os.rename(src, dst)
            i += 1
    except (FileExistsError,FileNotFoundError):
        pass
        # 다음 인덱스로 넘어가지 않고 재귀하기


import random

print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))

import datetime

today = datetime.datetime.now()
print(today)
print(today.strftime("%A %B %dth %Y"))
print(type(today))