import random


# 사용자의 로또 번호 뽑기
def generate_numbers(num_length):
    myLottoNumber = []
    random_number = random.randint(1, 45)
    for number in range(num_length):
        while random_number in myLottoNumber:
            random_number = random.randint(1, 45)
        myLottoNumber.append(random_number)
    print(f"뽑은 번호 : {sorted(myLottoNumber)}")
    return sorted(myLottoNumber)


# 주최측의 로또 번호 생성
def draw_winning_numbers():
    winningNumbers = []
    random_number = random.randint(1, 45)
    for number in range(7):
        while random_number in winningNumbers:
            random_number = random.randint(1, 45)
        winningNumbers.append(random_number)

    result = sorted(winningNumbers[:6])
    result.append(winningNumbers[-1])
    print(f"추첨 번호 : {result[:6]}, 보너스 번호 : {result[-1]}")
    return result


# 주최측 로또 번호와 사용자의 로또 번호를 대조
def count_mathcing_numbers(userLottoNumber, winningNumbers):
    return len(set(userLottoNumber) & set(winningNumbers))


# 로또 보상 확인
def check(userLottoNumber, winningNumbers):
    result = count_mathcing_numbers(userLottoNumber, winningNumbers[:6])
    bonus_number = winningNumbers[-1]
    print(f"적중 개수 : {result} 개", end=" ..... ")
    if result <= 2:
        return 0
    elif result == 3:
        return 5000
    elif result == 4:
        return 50000
    elif result == 5 and bonus_number in userLottoNumber:
        return 50000000
    elif result == 5:
        return 1000000
    elif result == 6:
        return 1000000000

import inspect, os.path

filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
print(path)