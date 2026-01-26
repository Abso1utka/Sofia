balance = 1000

while True:
    print("--- МЕНЮ ---")
    print("1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")

    choice = int(input("Выберите операцию: "))

    if choice == 1:
        print("Ваш баланс:")
        print(balance)

    elif choice == 2:
        if balance >= 100:
            balance = balance - 100
            print("Снято")
        else:
            print("Недостаточно средств")

    elif choice == 3:
        balance = balance + 100
        print("Баланс пополнен")

    elif choice == 4:
        print("До свидания")
        break

    else:
        print("Неверная команда")