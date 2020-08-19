# 041 upper 메서드
ticker = "btc_krw"
print(ticker.upper())


# 042 lower 메서드
ticker1 = ticker.upper()
print(ticker1)
print(ticker1.lower())


# 043 capitalize 메서드      # >><<>><<>><<>><<>>>><<>><<>><<>><<>>>><<>><<>><<>><<>>
string = 'hello'
string.capitalize()         # 첫글자 대문자 지리네~ 내일되면 백프로 까먹는다 케케


# 044 endswith 메서드      # >><<>><<>><<>><<>>>><<>><<>><<>><<>>>><<>><<>><<>><<>>
file_name = "report.xlsx"
file_name.endswith("xlsx")  # 해당 문자로 끝나면 True 반환


# 045 endswith 메서드
file_name = "보고서.xlsx"
file_name.endswith(("xlsx" or "xls"))


# 046 startswith 메서드
file_name = "2020_report.xlsx"
file_name.startswith("2020")


# 047 split 메서드
a = "hello world"
a = a.split(" ")
print(a)

# 048 split 메서드
ticker = "btc_krw"
ticker.split("_")


# 049 split 메서드
date = "2020-05-01"
date.split("-")
year = date[0]
month = date[1]
day = date[2]


# 050 rstrip 메서드
data = "030123    "
data.rstrip()
data.rstrip(" 123")
