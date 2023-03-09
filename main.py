m = 0

for i in range(100):
    x = input('Введите целое число или Стоп -> ')
    try:
        m = m + int(x)
    except ValueError:
        if(type(x) is str and x=='Стоп'):
                print('Сумма чисел равна',m)
                break
        else:
            print('Ошибка преобразования типов')