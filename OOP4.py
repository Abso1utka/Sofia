class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def show_info(self):
        print(self.name)
        print(f"❤️: {self.hp}")
        print(f"⚔️: {self.dmg}")

# Создание объекта и вывод информации
gargoyle = Monster("Горгулья", 120, 18)
gargoyle.show_info()
