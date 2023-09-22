# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


def simplify_fraction(numerator, denominator):
    # Находим наибольший общий делитель числителя и знаменателя
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Упрощаем дробь, деля числитель и знаменатель на их НОД
    gcd_value = gcd(numerator, denominator)
    numerator //= gcd_value
    denominator //= gcd_value

    return numerator, denominator


def add_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split("/"))
    numerator2, denominator2 = map(int, fraction2.split("/"))

    # Проверяем, что знаменатель не равен нулю
    if denominator1 == 0 or denominator2 == 0:
        return "Ошибка! Знаменатель не может быть равен нулю."

    # Находим общий знаменатель
    common_denominator = denominator1 * denominator2

    # Приводим числители к общему знаменателю
    numerator1 *= denominator2
    numerator2 *= denominator1

    # Вычисляем сумму числителей
    sum_numerator = numerator1 + numerator2

    # Упрощаем полученную дробь
    simplified_numerator, simplified_denominator = simplify_fraction(sum_numerator, common_denominator)

    return f"{simplified_numerator}/{simplified_denominator}"


def multiply_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split("/"))
    numerator2, denominator2 = map(int, fraction2.split("/"))

    # Проверяем, что знаменатель не равен нулю
    if denominator1 == 0 or denominator2 == 0:
        return "Ошибка! Знаменатель не может быть равен нулю."

    # Умножаем числители и знаменатели
    product_numerator = numerator1 * numerator2
    product_denominator = denominator1 * denominator2

    # Упрощаем полученную дробь
    simplified_numerator, simplified_denominator = simplify_fraction(product_numerator, product_denominator)

    return f"{simplified_numerator}/{simplified_denominator}"


fraction1 = input("\nВведите первую дробь в формате числитель/знаменатель: ")
fraction2 = input("Введите вторую дробь в формате числитель/знаменатель: ")

sum_result = add_fractions(fraction1, fraction2)
product_result = multiply_fractions(fraction1, fraction2)

print("\nСумма дробей:", sum_result)
print("Произведение дробей:", product_result)

# Проверка результата с использованием модуля fractions

from fractions import Fraction

def add_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split("/"))
    numerator2, denominator2 = map(int, fraction2.split("/"))

    # Проверяем, что знаменатель не равен нулю
    if denominator1 == 0 or denominator2 == 0:
        return "Ошибка! Знаменатель не может быть равен нулю."

        # Создаем объекты Fraction для дробей
    Frac1 = Fraction(numerator1, denominator1)
    Frac2 = Fraction(numerator2, denominator2)

    sum_result = Frac1 + Frac2

    return str(sum_result)

def multiply_fractions(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split("/"))
    numerator2, denominator2 = map(int, fraction2.split("/"))

    # Проверяем, что знаменатель не равен нулю
    if denominator1 == 0 or denominator2 == 0:
        return "Ошибка! Знаменатель не может быть равен нулю."

        # Создаем объекты Fraction для дробей
    Frac1 = Fraction(numerator1, denominator1)
    Frac2 = Fraction(numerator2, denominator2)

    product_result = Frac1 * Frac2

    return str(product_result)

print("\nПроверка с использованием модуля fractions")
print("Сумма дробей:", (sum_result))
print("Произведение дробей:", (product_result))