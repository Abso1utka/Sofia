word = input("Введите слово: ")

# Преобразуем строку в список символов
letters = list(word)

# Перевёрнутая копия через срез [::-1]
reversed_letters = letters[::-1]

# Сравниваем исходный и перевёрнутый списки
if letters == reversed_letters:
    print(f"'{word}' – это палиндром")
else:
    print(f"'{word}' – не палиндром")