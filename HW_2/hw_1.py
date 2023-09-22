# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def int_to_hex(n):
    digits = "0123456789ABCDEF"
    hex_string = ""
    while n > 0:
        remainder = n % 16
        hex_digit = digits[remainder]
        hex_string = hex_digit + hex_string
        n = n // 16
    return hex_string

number = int(input("Введите целое число: "))
hex_representation = int_to_hex(number)
print("Число", int(number), "в шестнадцатеричном представлении будет 0x" + hex_representation)


# Проверка результата с использованием функции hex

numb = number

hexcalc = hex(numb)
print("\nПроверка результата с использованием функции hex!")
print("Число", int(numb), "в шестнадцатеричном представлении будет", hexcalc)