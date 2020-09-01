
file = open(file="C:/Users/leeja/WorkSpace/Python/Python Project/sub/chicken.txt",
            mode='r',
            encoding="utf-8")

thisMonth = file.readlines()
sales = 0
for thisDay in thisMonth:
    thisDay = thisDay.split(": ")
    sale = int(thisDay[1])
    sales += sale
    
print(sales/len(thisMonth))