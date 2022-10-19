def summator(num1,num2):
    summs=''
    summ0=0
    maxnum =  max(num1,num2)
    minnum =  min(num1,num2)
    if len(maxnum)!=len(minnum):
        dif = abs(len(maxnum)-len(minnum))
        minnum='0'*dif+minnum
    for i in range(len(maxnum)):
        el1=maxnum[len(maxnum)-i-1]
        el2=minnum[len(minnum)-i-1]
        summ = int(el1)+int(el2)+summ0
        if summ==2:
            summ0= 1
            summs='0'+summs
        elif summ==3:
            summ0= 1
            summs='1'+summs
        else:
            summ0=0
            summs=str(summ)+summs
    if summs[0]!='0':
        print('Первоначально:',summs)
        nnumba=''
        indict={'0':'1','1':'0'}
        for i in summs:
            nnumba+=indict[i]
        summs=nnumba
    return '['+str(summ0)+']'+' '+summs
while True:
    num1=input()
    num2=input()
    numba = summator(num1,num2)
    print(numba)

