import random

# Генерируем список из 5 случайных чисел (для наглядности)
A = [random.randint(1, 100) for _ in range(5)]
print(f"Исходный список: {A}")

# Ищем индекс минимального элемента вручную (чтобы не использовать .index())
min_val = A[0]
min_idx = 0
for i in range(1, len(A)):
    if A[i] < min_val:
        min_val = A[i]
        min_idx = i

# Меняем местами первый элемент и минимальный
A[0], A[min_idx] = A[min_idx], A[0]

print(f"После обмена: {A}")