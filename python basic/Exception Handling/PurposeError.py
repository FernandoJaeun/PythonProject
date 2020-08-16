# 에러 일부러 발생시키기 !!?

class Bird:
    def fly(self):
        raise NotImplementedError   # 일부러 발생시키기 이잉!?
        # 꼭 구현해야하는 부분이 작성되지 않고 지나칠 때 그 사실을 알리기 위해 에러를 띄운다카더라

class Eagle(Bird):
    def fly(self):
        print("baby eagle") # 오버라이드로 작성하면 에러가 뜨지 않는다!!! 굳~~

eagle = Eagle()
eagle.fly()
