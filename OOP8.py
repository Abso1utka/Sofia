class DarkEntity:
    def __init__(self, name, species, danger_level):
        self.__name = name
        self.__species = species
        self.__danger_level = danger_level

boss = DarkEntity("Балор", "Высший Демон", 99)

# Обход инкапсуляции через name mangling
print(f"Данные из Гримуара: {boss._DarkEntity__name}, {boss._DarkEntity__species}, {boss._DarkEntity__danger_level}")