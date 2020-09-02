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
    # count = 0
    # for userPick in userLottoNumber:
    #     if userPick in winningNumbers:
    #         count +=1
    # return count


def check_reward(userLottoNumber, winningNumbers):
    # winningNumbers_main = winningNumbers[0:6]
    # winningNumbers_bonus = winningNumbers[-1]
    # result = len(set(userLottoNumber).intersection(set(winningNumbers_main)))

    result = count_mathcing_numbers(userLottoNumber, winningNumbers[:6])
    bonus_number = winningNumbers[-1]
    print(f"적중 개수 : {result} 개", end=" ..... ")
    if result <= 2:
        return "꽝!"
    elif result == 3:
        return "5등, 상금 5천원"
    elif result == 4:
        return "4등, 상금 5만원"
    elif result == 5 and bonus_number in userLottoNumber:
        return "2등, 상금 5천만원"
    elif result == 5:
        return "3등, 상금 100만원"
    elif result == 6:
        return "1등, 상금 10억원"
    else:
        return "오류가 있습니다"

print(check_reward(generate_numbers(6), draw_winning_numbers()))
# print(check_reward([1,2,3,4,5,6],[1,2,3,4,5,8,7]))

# condition = 0
# count = 0
# while condition <= 5:
#     condition = count_mathcing_numbers(
#         generate_numbers(6), draw_winning_numbers())
#     print(condition)
#     count += 1

# print(f"무려 {count}번 만에 3등")
