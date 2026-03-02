for b in range(1, 11):
    for c in range(1, 21):
        for t in range(1, 201):

            if (b + c + t == 100) and (10 * b + 5 * c + 0.5 * t == 100):
                print(f"Быков: {b}, Коров: {c}, Телят: {t}")