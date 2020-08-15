coffee = 10
cafuchino = 10
buy = {'coffee': 0, 'cafuchino': 0}
lineUp = list(buy.keys())
money = 0
print("사먹을 수 있는 제품 : ", lineUp)
while True:
    if(money < 300):
        money = int(input("돈을 입력하세요 : "))
    if(money < 300): 
        if(input("사먹을 수 있는 제품이 없습니다. 돈을 더 넣으시겠습니까? (Y/N) : ") == 'Y'):
            pass
        else:
            print("가게에서 나갑니다")
            break
    if(money >= 1000):
        if(input("cafuchino 를 구매하시겠습니까? (Y/N) : ") == 'Y'):
            money -=1000
            cafuchino -= 1
            buy['cafuchino'] += 1
            print("cafuchino 1잔을 구매하였습니다")
    if(money >= 300):
        if(input("coffee 를 구매하시겠습니까? (Y/N) : ") == 'Y'):
            money -= 300
            coffee -= 1
            buy['coffee'] += 1
            print("coffee 1잔을 구매하였습니다")
    if(money<300):
        if(input("돈을 다썼습니다 가게에서 나가시겠습니까? (Y/N) : ") == 'Y'):
            break
        else:
            pass
print("구매내역 : ", buy)    
