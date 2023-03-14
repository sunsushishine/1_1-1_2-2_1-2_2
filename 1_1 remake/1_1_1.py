num = 0

while True:
    temp = input("Введите целое число или Стоп -> ")
    try:
        num = num + int(temp)
    except ValueError:
        if(type(temp) is str and num == 'Стоп' or 'стоп'):
            print("Сумма чисел равна:", num)
            break
        else:
            print("Ошибку преобразования типов")
