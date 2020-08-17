import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.
import time



def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Strat")

threads = []        # 쓰레드 생성
for i in range(5):
    t = threading.Thread(target=long_task)      # 쓰레드 지정
    threads.append(t)       # 쓰레드 저장


for t in threads:
    t.start()           # 쓰레드 시작

for t in threads:
    t.join()        # 쓰레드가 하나씩 모여서 다 채워지면 끝난다

print("End")
