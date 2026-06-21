correct_pin = 4590

while True:
    user_input = int(input("Введите пин-код: "))

    if user_input == correct_pin:
        print("Доступ разрешен")
        break
    else:
        print("Ошибка. Попробуйте еще раз")