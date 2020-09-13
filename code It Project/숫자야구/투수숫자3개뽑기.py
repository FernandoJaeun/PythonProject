from random import randint


def generate_numbers():
    numbers = []
    
    for i in range(3):
        randomNumber = randint(0,9)    
        while randomNumber in numbers:
            randomNumber = randint(0,9)
        numbers.append(randomNumber)
        
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers
print(generate_numbers())