count = 0
counting = False
name = ""

while True:
    name = input("Введите имя игрока: ")

    if name == "Левон": # встретили Левона = завершаем
        break

    if counting: # встретили Александру = увеличиваем счетчик
        count += 1

    if name == "Александра":
        counting = True # Если встретили Александру, включаем флаг для следующих итераций

print(f"{count}")