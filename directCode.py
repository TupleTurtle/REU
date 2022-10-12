#Лукьянов Андрей Николаевич 4115
def codify(num):
    indict={'0':'1','1':'0'}
    if num<128 and num>-128:
        if num<0:
# прямой код отрицательного числа:
            num=str(bin(num))[3:]
            numb=''
            dif=7-len(num)
            while dif!=0:
                num='0'+num
                dif=dif-1
# получение обратного кода:
            for i in num:
                numb+=indict[i]
            num='1'+numb
# довод до дополнительного кода:
            num=int(num,2)+1
            num=bin(num)[2:]
        else:
# прямой код положительного числа:
            num=str(bin(num))[2:]
            dif=8-len(num)
            while dif!=0:
                num='0'+num
                dif=dif-1
        return(num)
    else:
        return 'Число невозможно представить в прямом коде с помощью 8 бит'
while True:
    number = int(input('Введите число в диапазоне [-127;127]: '))
    print(codify(number))
