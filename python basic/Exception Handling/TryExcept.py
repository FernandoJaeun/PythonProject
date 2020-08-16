try:
    pass    # 이 부분을 먼저 실행한다
    # 에러가 발생하지 않는다면 except문을 지나친다
except expression as identifier:     # 에러가 발생했을 때 에러 내용을 담은 identifier 변수를 만든다.
    pass

try:
    pass
except expression:  # 에러가 발생하면 코드를 실행한다
    pass

try:
    4/0
except ZeroDivisionError as e:
    print(e)    # 에러내용이 출력


## 여러 개의 에러 동시에 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e: # 에러를 한대 모았음
    print(e)
 
