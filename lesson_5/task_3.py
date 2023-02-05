name_age = input('Введите свое имя и возраст через пробел: ')
name_age_a = name_age.split()
name, age_1 = name_age_a[0], name_age_a[1]

while age_1.isdigit() == True: # проверяет, что введено число, а не какой-либо другой символ
    age = int(age_1)
    if age <= 0:
        print('Ошибка повторите ввод')
    elif 0 < age < 10:
        print(f'Привет шкет {name.title()}')
    elif 10 <= age <= 18:
        print(f'Как жизнь {name.title()}')
    elif 18 < age < 100:
        print(f'Что желаете {name.title()}')
    else:
        print(f'{name.title()}, вы лжете - в наше время столько не живут ... ')
else:
    print('Ошибка повторите ввод')