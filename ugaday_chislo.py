import random

xCh = random.randint(1, 101)
Ug = 0

print('___________________________')
print('Игра "Угадай число"')
print('Я загадал число от 1 до 100')
print()

while xCh != Ug:
    input_data = input('Введите число: ')

    if not input_data.isdigit():
        input_data = 0
    else:
        Ug = int(input_data)

    if input_data in (0, '0', '00'):
        print('Вы знаете секрет :-)')
        exit()
    elif Ug < xCh:
        print('Угадываемое больше Вашего\n')
    elif Ug > xCh:
        print('Угадываемое меньше Вашего\n')

else:
    print('Вы угадали число!!!', xCh)

print()
print('__________!МОЛОДЕЦ!___________')
