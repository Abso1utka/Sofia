for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            if 28 * n + 30 * k + 31 * m == 365:
                print(f"n (28 дней) = {n}, k (30 дней) = {k}, m (31 день) = {m}")