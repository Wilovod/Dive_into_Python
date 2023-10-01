# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
#
# Разбейте задачу на отдельные операции — функции.Дополнительно сохраняйте все операции поступления и снятия средств в список


def atm():
    balance = 0
    transaction_counter = 0
    total_withdrawn = 0
    is_max_balance_exceeded = False

    while True:
        print("\nВыберите действие:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Проверить баланс")
        print("4. Выйти")

        action = input("Введите номер действия: ")

        if action == "1":
            amount = int(input("\nВведите сумму для пополнения (кратную 50 у.е.): "))
            if amount % 50 != 0:
                print("Сумма должна быть кратной 50 у.е.")
                continue

            if is_max_balance_exceeded:
                amount *= 0.9

            balance += amount
            transaction_counter += 1
            print(f"Вы пополнили счет на {amount} у.е.")


        elif action == "2":

            print("\nКомиссия за снятие — 1.5%")

            amount = int(input("Введите сумму для снятия (кратную 50 у.е.): "))
            if amount % 50 != 0:
                print("Сумма должна быть кратной 50 у.е.")
                continue

            if is_max_balance_exceeded:
                amount *= 0.9

            if amount > balance:
                print("\nНедостаточно средств на счете")
                continue

            commission = max(30, min(amount * 0.015, 600))
            balance -= (amount + commission)
            transaction_counter += 1
            total_withdrawn += amount

            print(f"\nВы сняли {amount} у.е. (комиссия: {commission} у.е.)")
            print(f"\nБаланс: {balance} у.е.")

        elif action == "3":
            if is_max_balance_exceeded:
                amount *= 0.9

            print(f"\nБаланс: {balance} у.е.")

        elif action == "4":
            print(f"Итого снято: {total_withdrawn} у.е.")
            print(f"Окончательный баланс: {balance} у.е.")
            print("Спасибо за использование нашего банкомата, До свидания!!!")
            break

        else:
            print("Неверное действие, попробуйте снова")

        # Проверка на превышение максимального баланса
        if balance > 5000000:
            is_max_balance_exceeded = True
            balance *= 0.9


        # Предупреждение при следующей операции пополнения или снятия начисляются проценты - 3%
        if transaction_counter % 2 == 0:
            print("\nПредупреждение! При следующей операции пополнения или снятия наличных начислится процент в пользу банка!!! ")

        # Проверка на каждую третью операцию
        if transaction_counter % 3 == 0:
            balance *= 0.97
            print("\nНачислен процент за операцию!")

atm()