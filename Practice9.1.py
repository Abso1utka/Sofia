n = int(input("Введите число: "))

current_num = 1

while current_num <= n:
    if (5 <= current_num <= 9) or (17 <= current_num <= 37) or (78 <= current_num <= 87):
        current_num += 1
        continue

    print(f"{current_num}")

    current_num += 1