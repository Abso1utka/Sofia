price = int(input("Введите цену: "))

coins_count = 0

while price > 0:
    if price >= 25: # провека номинала от большего к меньшему
        price -= 25
    elif price >= 10:
        price -= 10
    elif price >= 5:
        price -= 5
    else:
        price -= 1

    coins_count += 1 # увеличиваем счётчик монет

print(f"{coins_count}")