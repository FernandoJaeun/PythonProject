# 271
import random


class Account:
    countOfAccount = 0
    countOfDeposit = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.withdrawHistory = []
        self.depositHistory = []
            
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        self.countOfAccount += 1
        self.accountInfo = []
        self.accountInfo.append(self.name)
        self.accountInfo.append(self.bank)
        self.accountInfo.append(self.balance)
        self.accountInfo.append(self.account_number)
        self.accountInfo.append(self.countOfAccount)

    def getAccountNum(self):
        return self.countOfAccount

    def deposit(self, into):
        self.balance += into
        self.countOfDeposit += 1
        if self.countOfDeposit % 5 == 0:
            self.balance += self.balance * 0.01
        self.depositHistory.append(into)

    def depositHistory(self):
        for i in self.depositHistory:
            print(i)

    def withdraw(self, out):
        self.balance -= out
        self.withdrawHistory.append(out)

    def withdrawHistory(self):
        return self.withdrawHistory

    def displayInfo(self):
        return self.accountInfo

    def __del__(self):
        self.countOfAccount -= 1


kim = Account("김민수", 100)
Lee = Account("이재윤", 200)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)


# 273
print(kim.countOfAccount)


# 274
kim.deposit(1000)
print(kim.balance)


# 275
kim.withdraw(100)
print(kim.balance)


# 276
print(kim.displayInfo())


# 277
for i in range(5):
    kim.deposit(200)
print(kim.displayInfo())

# 278
data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)
data.append(k)
data.append(l)
data.append(p)


# 279

for c in data:
    if c.balance >= 1000:
        c.deposit(1000)
        print(c.displayInfo())

# 280
k = Account("이재윤", 1000)
k.deposit(100)
k.deposit(100)
k.deposit(100)
k.deposit(100)
k.deposit(100)
k.depositHistory()
