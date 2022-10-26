def binSum(num1,num2):
    output = str(num1+num2).replace('12','100').replace('2','10')
    return output

def conjunction(table):
    output=''
    for line in table:
        out=''
        res = line.pop()
        if res==0:
            for i in range(len(line)):
                if line[i]==1:
                    out+='not(x'+str(i+1)+')+'
                else:
                    out+= 'x'+str(i+1)+'+'
            output=f'{output}*({out[:-1]})'
        print(line)
    return output[1:]

def fano(probabilities=False):
    dic = {}
    if not probabilities:
        probabilities = [1/len(alphabet)]*len(alphabet)
    dic = dict(zip(alphabet, probabilities))
    dic = dict(sorted(dic.items(), key=lambda x:x[1]))
    while len(dic)!=1:
        space = '                       '*len(dic)
        keys = list(dic.keys())
        print(keys[0]+space+keys[1])
        items= list(dic.items())
        p1,v1 = items[0]
        p2,v2 = items[1]
        dic.pop(keys[0])
        dic.pop(keys[1])
        dic={**{p1+'+'+p2: v1+v2},**dic}
        dic = dict(sorted(dic.items(), key=lambda x:x[1]))
fano(['а','б','в','г'], [0.30,0.30,0.30,0.10])

def disjunction(table):
    output=''
    for line in table:
        out=''
        res = line.pop()
        if res==1:
            for i in range(len(line)):
                if line[i]==0:
                    out+= 'not(x'+str(i+1)+')*'
                else:
                    out+= 'x'+str(i+1)+'*'
            output=f'{output}+{out[:-1]}'
        print(line)
    return output[1:]



def decrCC(num,cc, precision):
    output=''
    if '.' in str(num):
        whole,fract=str(num).split('.')
        fract='0.'+fract
        while precision>0:
            fract=float(fract)*2
            fract=str(fract).split('.')
            output=output+fract[0]
            fract='0.'+fract[1]
            precision=precision-1
        output='.'+output
        num=int(whole)
    while num!=0:
        output=str(num%cc)+output
        num=num//cc
    return output



def incrCC(num, cc):
    output=0
    num=str(num)
    if '.' in num:
        whole,fract=num.split('.')
        for i in range(len(fract)):
            output+=int(fract[i])*cc**(-(i+1))
            num=whole
    leng=len(num)
    for i in range(leng):
        output+=int(num[i])*cc**(leng-i-1)
    return output



def ln(x):
    n=100000
    return n*(x**(1/n)-1)



def log(base, x):
    return ln(x)/ln(base)


def entropy(signal,noise):
    return -log(2, signal/noise)




def mesgInf(mesgLength, alphabetLength):
    return mesgLength*log(2, alphabetLength)

def roundUp(num):
    return -(-num//1)



def hexdecCC(num):
    output=''
    num=str(num)
    dic={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    dif = len(num)%4
    if dif:
        num='0'*(4-dif)+num
    while num!='':
        output=output+dic[num[0:4]]
        num=num[4:]
    return output


def hexCC(num):
    output=''
    num=str(num)
    dic={'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}
    dif = len(num)%3
    if dif:
        num='0'*(3-dif)+num
    while num!='':
        output=output+dic[num[0:3]]
        num=num[3:]
    return output

def binHex(num):
    output=''
    num=str(num)
    dic={'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
    for el in num:
        output=output+dic[el]
    return output

def binHexdec(num):
    output=''
    num=str(num)
    dic={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    for el in num:
        output=output+dic[el]
    return output


def totalEntropy(states):
    return sum(map(lambda x: x[0]/x[1]*entropy(x[0],x[1]), states))

def polar(num):
    newNum=''
    switch = {'0':'1','1':'0'}
    for el in num:
        newNum=newNum+switch[el]
    return newNum

def directCode(num):
    code=decrCC(abs(num),2)
    leng=len(code)
    if abs(num)<128:
        byteNum=8
    else:
        byteNum=16
    dif=byteNum-leng%byteNum-1
    code='0'*dif+code
    if num<0:
        return binSum(int('1'+polar(code)),1)
    else:
        return '0'+code

