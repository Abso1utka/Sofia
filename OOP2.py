class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстр: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")

# Считывание данных для двух монстров
line1 = input().split()
line2 = input().split()

# Извлечение параметров
name1, hp1, dmg1 = line1[0], int(line1[1]), int(line1[2])
name2, hp2, dmg2 = line2[0], int(line2[1]), int(line2[2])

# Создание объектов
m1 = Monster(name1, hp1, dmg1)
m2 = Monster(name2, hp2, dmg2)