# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0  # Нижняя граница случайного числа
UPPER_LIMIT = 1000  # Верхняя граница случайного числа
MAX_TRIES = 10  # Максимальное количество попыток

num = randint(LOWER_LIMIT, UPPER_LIMIT)
tries = 0

print("Программа загадала число от 0 до 1000. Попробуйте угадать его за 10 попыток!")

while tries < MAX_TRIES:
    guess = int(input("Введите вашу попытку: "))
    tries += 1

    if guess == num:
        print("Поздравляю, вы угадали число!")
        break
    elif guess < num:
        print("Загаданное число больше вашей попытки.")
    else:
        print("Загаданное число меньше вашей попытки.")

    if tries == MAX_TRIES:
        print("К сожалению, вы исчерпали все попытки. Загаданное число было", num)