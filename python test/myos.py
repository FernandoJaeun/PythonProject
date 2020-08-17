import os
import glob
import time
import random

os.chdir("C:/Users/leeja/WorkSpace/Python/Python Project")
result = os.popen("dir")
print(result.read())

b = glob.glob("C:/Users/leeja/WorkSpace/Python/Python Project/*.py")
for i in b:
    print(i)

time.strftime('%x %X')
# 풀이
time.strftime(' %Y / %m / %d   %H:%M:%S')



data = []
for i in range(1, 46):
    data.append(i)

def choiceNumber(data):
    number = data.pop(random.randint(0, len(data)-1))
    if number:
        return number
    else:
        choiceNumber(data)

choice = []
while len(choice) < 6:
    choice.append(choiceNumber(data))
print(choice)

# 풀이

result = []

while len(result) < 6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)