import random


def createNumber():                 # 랜덤 숫자를 생성하는 메소드
    return random.randint(1, 20)


number = createNumber()  # 랜덤 숫자 하나를 제비 뽑기
bullet = 4              # 게임 가능 횟수
gameLength = 4          # 게임의 길이(몇 회 반복인지 나타냄)
setionJump = ".\n.\n."  # 정답을 맞출 시 출력문 사이 간격 조절용

for i in range(gameLength):
    noticeMessage = f"기회가 {bullet}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: "
    userPick = int(input(noticeMessage))    # 유저의 선택은?
    bullet -= 1                             # 유저가 숫자를 하나 뽑을 때마다 기회 하나를 소멸

    if userPick == number:                  # 정답일 경우,
        print(setionJump)
        print(f"정답입니다 {gameLength-bullet}번 만에 마추셨습니다")
        break                               # 게임 종료
    if userPick > number:                   # 친절하게 정답의 방향을 알려줌
        print("Down", end="  ")
        print(f"사용 기회:{gameLength-bullet}\n")
    else:
        print("UP", end="  ")
        print(f"사용 기회:{gameLength-bullet}\n")

if bullet == 0:                             # 기회를 모두 썻지만, 정답을 맞추지 못했을 경우, 게임 종료 문구
    print("------------게임 종료-----------\n맞추지 못했습니다 수고하셨습니다")
else:                                       # 기회가 남아있을 때 맞췄을 경우, 게임 종료 문구
    print("------------게임 종료-----------")
