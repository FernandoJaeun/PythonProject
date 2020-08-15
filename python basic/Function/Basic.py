def add(a, b):
    return a+b

a = add(a= 1, b =2) # 매개변수를 지정하여 값을 할당하는 점이 간편하고 직관적이다!
a = add(b=1, a=2)   # 이렇게 매개변수를 지정하여 값을 할당하면 순서가 상관없다!



def something(*args):   # 매개변수를 몇 개 지정할 지 모르겠다면 뭉탱이로 던져줘라!
    for arg in args:    # something(1,2,3,4,5,6)
        print(arg)      # something(1,2,3,4) 모두 가능!

something(1,2,3,4,5,6)



def newSomething(choice, *args):        # 뭉탱이 매개변수와 단일 매개변수를 섞어 사용가능한 모습
    a = 0
    if choice =="add":
        for v in args:
            a += v
    elif choice =="multiple":
        a = 1
        for v in args:
            a *= v
    else:
        a = -1

    return a
multiple = "multiple"   
add = "add"



print(newSomething(multiple,1,2,3,4,5))

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(age= 3, name = "Fercho", address = "seoul")    # 딕셔너리 형태로 값을 반환해주는 키워드 매개변수



def add_multiple(a,b):
    return a+b, a*b         # 한번에 복수의 값을 리턴할 수 있는 튜플 리턴

print(add_multiple(3,7))



def alreadyParameter(name, old, man = True):    # 이런건 첨보는데, 매개변수에 초기값을 넣어준다라!! 대박!
    print("나의 이름은 %s 입니다" % name)         # 만약 초기값을 설정한다면 매개변수 젤 뒤쪽에 배치시켜야 오류가 생기지 않으니 주의!!!!
    print("나의 나이는 %s세 입니다" % old)

    if man:
        print("나는 남자입니다")
    else:
        print("나는 여자입니다")
name = "이재윤"
old = 26
man = True
woman = False
alreadyParameter(name, old, man)
alreadyParameter(name, old, woman)

