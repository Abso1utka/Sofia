numbers = [10, 20, 30, 40, 50]
search = int(input("Введите число для поиска: "))

found = False

# Перебор индексов через range(len(numbers))
for i in range(len(numbers)):
    if numbers[i] == search:
        print(f"Число {search} найдено на индексе {i}")
        found = True
        break       # немедленно выходим из цикла

if not found:
    print("Нет такого числа")