add = lambda a,b: a+b
result = add(3,4)
print(result)


# 위 람다식은 아래 def로 작성한 함수와 완전히 같은 기능을 한다.
# 람다는 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.
# def를 사용할 수 없는 곳????

def add(a, b):
    return a+b
result = add(3, 4)
print(result)