# 간단한 메모장 만들기
# 필요한 것
# 1. 기능
#   1.1 메모 추가하기
#   1.2 메모 조회하기
# 2. 입력
#   2.1 메모 내용
#   2.2 프로그램 실행 옵션
# 3. 출력
#   3.1 memo.txt 형식

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    file = open('temp1.txt', 'a')    
    file.write(memo+'\n')
    file.close()

if option == '-v':
    file = open('temp1.txt')
    memo = file.read()
    file.close()
    print(memo)