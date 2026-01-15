num = int(input("Введите исходное число: "))

original_last_digit = num % 10 # Запоминаем последнюю цифру исходного числа
count_3 = 0
count_last_digit_occurrences = 0
count_even = 0
sum_gt_5 = 0
prod_gt_7 = 1
has_digits_gt_7 = False # Флаг для понимания, были ли вообще цифры больше 7
count_0_5 = 0

while num > 0:
    digit = num % 10 # текущую последняя цифру

    if digit == 3: # Количество цифр 3
        count_3 += 1

    if digit == original_last_digit: # количество последней цифры
        count_last_digit_occurrences += 1

    if digit % 2 == 0: #количество чётных цифр
        count_even += 1

    if digit > 5: # Сумма цифр которые больше 5
        sum_gt_5 += digit

    if digit > 7: # Произведение цифр которые больше 7
        prod_gt_7 *= digit
        has_digits_gt_7 = True

    if digit == 0 or digit == 5: # проверка сколько раз встречаются 0 и 5
        count_0_5 += 1

    num //= 10 # убираем(откидываем) последнюю цифру

print(f"{count_3}")
print(f"{count_last_digit_occurrences}")
print(f"{count_even}")
print(f"{sum_gt_5}")
print(f"{prod_gt_7}")
print(f"{count_0_5}")