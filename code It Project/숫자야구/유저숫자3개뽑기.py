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

print(take_guess())