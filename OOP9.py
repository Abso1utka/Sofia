class Vampire:
    def __init__(self, name, bloodlust):
        self.__name = name
        self.__bloodlust = bloodlust

    def get_bloodlust(self):
        return self.__bloodlust

    def set_bloodlust(self, value):
        if 0 <= value <= 100:
            self.__bloodlust = value
        else:
            print("Ошибка: уровень жажды крови должен быть от 0 до 100!")

# --- пример использования ---
v = Vampire("Дракула", 50)
print("Текущая жажда:", v.get_bloodlust())   # 50

v.set_bloodlust(10)
print("Жажда после попытки установить 10:", v.get_bloodlust())

v.set_bloodlust(80)
print("Жажда после установки 80:", v.get_bloodlust())