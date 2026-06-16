users = ['Admin', 'Guest', 'User', 'Bot']

# Замена 'User' на 'Moderator' (индекс 2)
users[2] = 'Moderator'

# Замена 'Bot' на 'SuperAdmin' (отрицательный индекс -1)
users[-1] = 'SuperAdmin'

# Добавление 'Newbie' в конец через конкатенацию списков
users += ['Newbie']          # альтернатива: users = users + ['Newbie']

print(f"Итоговый список пользователей: {users}")