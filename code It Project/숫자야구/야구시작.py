from random import randint


def generate_numbers():
    numbers = []
    
    for i in range(3):
        randomNumber = randint(1,9)    
        while randomNumber in numbers:
            randomNumber = randint(1,9)
        numbers.append(randomNumber)
        
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    print(numbers)
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    while len(new_guess) < 3:
        picked_number = int(input(f"{len(new_guess)+1} 번째 숫자를 뽑으세요 : "))
        if picked_number > 9 or picked_number < 1:
            print("범위를 벗어났습니다. 다시 뽑아주세요")
        elif picked_number in new_guess:
            print("이미 뽑은 숫자입니다. 다시 뽑아주세요")
        else:
            new_guess.append(picked_number)
    
    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] == 0:
            continue
        else:
            ball_count += 1
            
    return strike_count, ball_count

strike, ball =  0, 0
count = 0
while strike != 3 :
    strike, ball = get_score(solution=generate_numbers(), guess= take_guess())
    count += 1
    if strike == 3 and ball == 0:
        print("축하합니다 3개 일치", count)
    else :
        print("불일치")