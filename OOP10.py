class Inventory:
    def __init__(self, gold):
        self.__gold = gold

    def get_gold(self):
        return f"В кошеле: {self.__gold} проклятых монет"

    def change_gold(self, amount):
        if self.__gold + amount < 0:
            print("Недостаточно золота для сделки!")
        else:
            self.__gold += amount

# --- Проверка работы ---
inv = Inventory(100)
print(inv.get_gold())

inv.change_gold(50)
print(inv.get_gold())

inv.change_gold(-30)
print(inv.get_gold())

inv.change_gold(-200)
print(inv.get_gold())