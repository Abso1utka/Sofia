class Werewolf:
    def __init__(self, name):
        self.__name = name
        self.__form = "Человек"
        self.__power = 15

    def get_stats(self):
        print(f"{self.__name} сейчас в форме: {self.__form}. Сила: {self.__power}")

    def transform(self):
        if self.__form == "Человек":
            self.__form = "Волк"
            self.__power = 45
            print(f"{self.__name} обрастает шерстью!")
        else:  # форма "Волк"
            self.__form = "Человек"
            self.__power = 15
            print(f"{self.__name} снова становится человеком.")

# --- Проверка ---
w = Werewolf("Люпен")
w.get_stats()      # Человек, сила 15
w.transform()      # В волка
w.get_stats()      # Волк, сила 45
w.transform()      # Обратно в человека
w.get_stats()      # Человек, сила 15