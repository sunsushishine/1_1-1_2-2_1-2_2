import random

CountD = 0
CountL = 0
CountW = 0
l = ['k','n','b'] 

def inp(): 
    global n
    while True:
        try:
            n = int(input('Введите количество игр: '))
            return n
        except ValueError:
            print('Это не число!')

def logic(x, y): 
    global CountD, CountW, CountL
    if x == y:
        print('Ничья')
        CountD += 1
    elif (x == 'k' and y == 'n') or (x == 'n' and y == 'b') or (x == 'b' and y == 'k'):
        print('Выигрыш')
        CountW += 1
    else:
        print('Проигрыш')
        CountL += 1      
    return CountD, CountL, CountW

inp()
while n != 0:
    while True:
        x = input('Камень (k), Ножницы (n), Бумага (b) -> ')
        if x not in l:
            print('Введите k, n, b!')
        else: break

    y = random.choice(l)
    logic(x, y)
    n -= 1
else:
    print('Победы - {0}\nПроигрыши - {1}\nНичьи- {2}'.format(CountW, CountL, CountD))
