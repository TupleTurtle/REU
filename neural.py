
alp = input('алфавит через пробел: ').split(' ')
ifProbs = input('введите 1, если даны вероятности: ')
dic = {}
if ifProbs==str(1):
    probs = map(float,input('вероятности через пробел: ').split(' '))
else:
    probs = [1/len(alp)]*len(alp)
dic = dict(zip(alp, probs))
dic = dict(sorted(dic.items(), key=lambda x:x[1]))
print(dic)
while len(dic)!=1:
    space = '           '*len(dic)
    keys = list(dic.keys())
    print(keys[0]+space+keys[1])
    items= list(dic.items())
    p1,v1 = items[0]
    p2,v2 = items[1]
    if v1>1:
        order = v11//1
        v1=v1%1
    elif v2>1:
        order = v2//1
        v2=v2%1
    dic.pop(keys[0])
    dic.pop(keys[1])
    dic={**{p1+'+'+p2: v1+v2},**dic}
    dic = dict(sorted(dic.items(), key=lambda x:x[1]))



