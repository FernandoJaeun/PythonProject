prompt = """
"Choose one"
1. Add
2. Del
3. List
4. Quit

Enter number : """

list = ["이재윤" , "최서윤"]
newMember = ""
delMember = 0
number = 0
while True:
    print(prompt)
    number = int(input())
    if(number == 1):
        newMember= input("추가할 멤버의 이름을 입력하세요 : ")
        list.append(newMember)
        break
    if(number ==2):
        delMember = input("삭제할 항목의 번호를 입력하세요 : ")
        delMember = int(delMember)-1
        print(delMember)
        del list[delMember]
        break
    if(number == 3):
        print(list)
        break
    if(number == 4):
        break
print(list)