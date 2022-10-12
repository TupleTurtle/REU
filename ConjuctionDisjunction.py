#Лукьянов Андрей Николаевич 4115

    # Все Функции:
#выбор между СДНФ и СКНФ
def rule(num):
    table = input("введите таблицу, используя запятые для разделения строк: ")
    table=table.split(',')
    if num=='0':
        print(dis(table))
    elif num=='1':
        print(con(table))
    else:
        print('Не верно указан тип операции')
    
#Нахождение элементарной конъюнкции строки для СДНФ:
def lineDis(line):
    out=''
    line = line.split()
    res = line.pop()
    if res=='1':
        for i in range(len(line)):
            if line[i]=='0':
                out+= 'not(x'+str(i+1)+')*'
            else:
                out+= 'x'+str(i+1)+'*'
        out=out[:-1]
    return out+'+'

#Нахождение СДНФ
def dis(table):
    finOut=''
    for line in table:
        finOut+=lineDis(line)
    return finOut[:-1]

#Нахождение элементарной дизъюнкции строки для СКНФ:
def lineCon(line):
    out=''
    line = line.split()
    res = line.pop()
    if res=='0':
        for i in range(len(line)):
            if line[i]=='1':
                out+='not(x'+str(i+1)+')+'
            else:
                out+= 'x'+str(i+1)+'+'
        out=out[:-1]
    return '('+out+')*'

#Нахождение СКНФ:
def con(table):
    finOut=''
    for line in table:
        finOut+=lineCon(line)
    return finOut[:-1]

    #Запуск программы:
cmd = input('Введите 0 для получения СДНФ, 1 для СКНФ: ')
rule(cmd)
