n = int(input("Введите натуральное число: "))

last_digit = n % 10

count_3 = 0
count_last = 0
count_even = 0
sum_gt_5 = 0
prod_gt_7 = 1
has_gt_7 = False
count_0_and_5 = 0

temp = n
while temp > 0:
    digit = temp % 10

    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_gt_5 += digit
    if digit > 7:
        prod_gt_7 *= digit
        has_gt_7 = True
    if digit == 0 or digit == 5:
        count_0_and_5 += 1

    temp //= 10

if not has_gt_7:
    prod_gt_7 = 1

print(count_3)
print(count_last)
print(count_even)
print(sum_gt_5)
print(prod_gt_7)
print(count_0_and_5)