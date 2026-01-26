total_sum = 0

while True:
    price = int(input("Введите цену товара (0 для завершения): "))

    if price == 0:
        break

    if price < 0:
        print("Ошибка цены")
        continue

    total_sum = total_sum + price

if total_sum > 1000:
    discount = total_sum * 10 / 100
    final_price = total_sum - discount
    print("Итоговая сумма со скидкой 10%:")
    print(final_price)
else:
    print("Итоговая сумма к оплате:")
    print(total_sum)