# # 021 문자열 인덱싱
# letters = 'python'
# print(letters[0], letters[2])   # 한 글자씩 가져오는 것을 '인덱싱'이라고 한다


# # 022 024 문자열 슬라이싱
# license_plate = "24가 2210"
# print(license_plate[-4])  # 일정 구간을 슬라이싱(slicing)해서 가져온다

# # string = 'PYTHON'
# string_reverse = []
# for i in string:
#     string_reverse.append(i)
# string_reverse.reverse()
# for i in string_reverse:
#     print(i, end="")
# print(string[::-1])  # 방향도 있구나!!!!!!


# # 023 문자열 인덱싱
# wow = "홀짝홀짝홀짝"
# print(wow[::2])


# # 025 문자열 치환
# phone_number = "010-1111-2222"
# phone_number.replace("-"," ")


# # 026 문자열 다루기
# phone_number2 = "010-1111-2222"
# phone_number2 = phone_number2.replace("-","")
# print(phone_number2)


# # 027 문자열 다루기
# url = "http://sharebook.kr"
# urldot = url.find(".")+1
# url[urldot:]

# urlsplit = url.split(".") # . 을 기준으로 조각 조각 나눈 다음 리스트로 저장
# urlsplit[1]


# # 028 문자열은 immutable
# lang = 'python'
# lang[0] = 'P'
# print(lang) # 결과는?
# # 문자열을 수정이 안된다, 그래서 immutable


# 029 replace 메서드
string = 'abcdfe2a354a32a'
string1 = string.replace("a","A")
print(string1)


# 030 replace 메서드
string = 'abcd'
string.replace('b', 'B')    # abcd , aBcd 두 개의 객체가 따로 따로 메모리에 할당된다. 문자열은 변경할 수 없는 자료형이기 때문이다.
print(string)