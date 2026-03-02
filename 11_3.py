powers = {i ** 5: i for i in range(1, 151)}
is_found = False

for a in range(1, 151):
    if is_found: break

    for b in range(a, 151):
        if is_found: break

        for c in range(b, 151):
            if is_found: break

            for d in range(c, 151):
                sum_powers = a ** 5 + b ** 5 + c ** 5 + d ** 5

                if sum_powers in powers:
                    e = powers[sum_powers]
                    print(f"Найдено опровержение! a={a}, b={b}, c={c}, d={d}, e={e}")
                    print(f"Сумма a+b+c+d+e = {a + b + c + d + e}")
                    is_found = True
                    break