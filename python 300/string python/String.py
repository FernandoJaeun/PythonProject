# # 021 문자열 인덱싱
# letters = 'python'
# print(letters[0], letters[2])   # 한 글자씩 가져오는 것을 '인덱싱'이라고 한다


# # 022 문자열 슬라이싱
# license_plate = "24가 2210"
# print(license_plate[-4])  # 일정 구간을 슬라이싱(slicing)해서 가져온다

string = 'PYTHON'
string_reverse = []
for i in string:
    string_reverse.append(i)
string_reverse.reverse()
for i in string_reverse:
    print(i, end="")

print(string[::-1]) # 방향도 있구나!!!!!!


# # 023 문자열 인덱싱
# wow = "홀짝홀짝홀짝"
# print(wow[::2])
