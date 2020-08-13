dic = {'name' : 'wodbs', 'age' : 26}
print(dic['name'])

dic['tall'] = 182
print(dic)

del dic['tall']
print(dic)

dic['name'] = "Fercho"
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

for k, c in dic.items():
    print(k)
    print(c)