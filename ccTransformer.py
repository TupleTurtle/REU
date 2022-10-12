# Лукьянов Андрей Николаевич 4115

# Повышение системы
def transform10cc(num, cc):
    if ',' in num:
        num=num.split(',')
        num1=num[0]
        num2=num[1]
        sum=0
        for i in range(len(num1)):
            power=(len(num1)-i-1)
            part = int(num1[i])*(int(cc)**(power))
            print(num1[i]+'*'+cc+'^'+str(power))
            sum+=part
        for i in range(len(num2)):
            power=-(len(num2)+i-1)
            part = int(num2[i])*(int(cc)**(power))
            print(num2[i]+'*'+cc+'^'+str(power))
            sum+=part
        print(sum)
    else:
        sum=0
        for i in range(len(num)):
            power=(len(num)-i-1)
            part = int(num[i])*(int(cc)**(power))
            print(num[i]+'*'+cc+'^'+str(power))
            sum+=part
        print(sum)

# Понижение системы
def bina(num,cc):
    if ',' in num:
        res=''
        num='.'.join(num.split(','))
        num=float(num)
        count=0
        while count<20:
            print(count,num, res)
            count+=1
            num=num*2
            if num>1:
                res+='1'
                num=num-1
            else:
                res+='0'
        return res
    else:
        num=int(num)
        cc=int(cc)
        res=''
        while num!=0:
            rem = str(num%cc)
            res+=rem
            p=num//cc
            print(str(num)+'/'+str(cc)+'='+str(p)+','+rem)
            num=p
        return res[::-1]
    
# Метод триад
def triad(num):
    total=''
    if ',' in num:
        num = num.remove(',')
    dic = {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
    for i in num:
        total+=dic[i]
        print(i,dic[i])
    print(total)
    
# Метод тэтрад
def tetrade(num):
    total=''
    if ',' in num:
        num = num.remove(',')
    dic = {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
    for i in num:
        total+=dic[i]
        print(i,dic[i])
    print(total)
while True:
    num = input()
    cc = input()
    ch=input()
    if ch=='1':
        transform10cc(num, cc)
    elif ch=='2':
        triad(num)
    else:
        print(bina(num,cc))
