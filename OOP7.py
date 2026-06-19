class Zombie:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def bite(self, damage):
        self.hp -= damage
        return self.hp

zombie = Zombie("Мясник", 100)

damage = int(input("Введите силу укуса:"))

print(f"Остаток здоровья: {zombie.bite(damage)}")