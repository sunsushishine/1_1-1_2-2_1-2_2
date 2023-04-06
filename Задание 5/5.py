import random

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

end_game = True

variants = ['камень', 'ножницы', 'бумага']

while end_game == True:
    # Запрос выбора игрока
    print("Выберите вариант:")
    for index, variant in enumerate(variants):
        print(f"{index + 1}. {variant}")
    player_choice_index = input()
    try:
        player_choice_index = int(player_choice_index)
    except ValueError:
        print("Вы ввели неправильный вариант. Попробуйте еще раз.")
        continue

    # Проверка выбора игрока
    if player_choice_index not in range(1, len(variants) + 1):
        print("Вы ввели неправильный вариант. Попробуйте еще раз.")
        continue
    player_choice = variants[player_choice_index - 1]

    # Выбор компьютера
    computer_choice = random.choice(variants)

    # Вывод выбора игрока и компьютера
    print("Вы выбрали:", player_choice)
    print("Компьютер выбрал:", computer_choice)

    # Определение победителя
    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 'камень' and computer_choice == 'ножницы') \
        or (player_choice == 'ножницы' and computer_choice == 'бумага') \
        or (player_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы победили!")
    else:
        print("Компьютер победил!")

    # Запрос на повтор игры
    while True:
        print("Хотите сыграть еще раз?:\n1.да\n2.нет")
        try:
            play_again = int(input())
            if play_again == 2:
                end_game = False
                break
            elif play_again == 1:
                print("Игра продолжается..")
                break
            else:
                print("Выберите вариант из представленных")
                continue
        except ValueError:
            print("Вы ввели неправильный вариант. Попробуйте еще раз.")
            continue
    
print("Спасибо за игру!")
