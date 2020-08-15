def getAverage(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

print(getAverage(1,2,3,4,5,6))