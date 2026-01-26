max_number = 0

while True:
    number = int(input("Введите натуральное число (0 для выхода): "))

    if number == 0:
        break

    if number > max_number:
        max_number = number
    else:
        pass

print("Самое большое число:")
print(max_number)