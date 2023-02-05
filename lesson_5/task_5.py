
user_number = int(input('Введите целое число от 1 до 100: '))
hidden_number = 57
count = 0 # Колличество раз которое понадобилось для угадывания
while user_number != hidden_number:
    count += 1
    if user_number < hidden_number:
        print("Ваше число меньше чем загаданное, попробуйте еще раз")
        user_number = int(input('Введите целое число от 1 до 100: '))
    elif user_number > 100:
        print('Вы вышли за рамки числового корридора, попробуйте еще раз')
        user_number = int(input('Введите целое число от 1 до 100: '))
    elif user_number > hidden_number:
        print('Ваше число больше чем загаданное, попробуйте еще раз')
        user_number = int(input('Введите целое число от 1 до 100: '))

print(f'Вы угадали загаданное число. Вы сделали это за {count} раз ')

