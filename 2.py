prices = [1500, 500, 2000, 3500, 1000, 4500]

# Без циклов – только встроенные функции
max_price = max(prices)
min_price = min(prices)
total = sum(prices)
average = total / len(prices)   # средняя цена

# Форматированный вывод
print(f"Самый дорогой товар: {max_price}")
print(f"Самый дешёвый товар: {min_price}")
print(f"Общая стоимость: {total}")
print(f"Средняя цена: {average:.2f}")   # округлим до двух знаков