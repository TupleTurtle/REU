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
# двоичное в шестнадцатеричное
def binToSixteen(num):
    total=''
    dic={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    difa = len(num)%4
    if difa!=0:
        num='0'*(4-difa)+num
    while num!='':
        print(num[0:4],':',dic[num[0:4]])
        total=total+dic[num[0:4]]
        num=num[4:]
    print(total)
while True:
    num = input()
    cc = input()
    ch=input('1 повышение до 10сс, 2 если метод триад, 0 если понижение из 10сс, 3 если из 2сс в 16сс ')
    if ch=='1':
        transform10cc(num, cc)
    elif ch=='2':
        triad(num)
    elif ch=='3':
        binToSixteen(num)
    else:
        print(bina(num,cc))
