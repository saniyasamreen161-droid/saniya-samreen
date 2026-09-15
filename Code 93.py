n = 4
for i in range(1, n + 1):
    num_digits = 2 * i - 1
    spaces = " " * (2 * (n - i))
    numbers = " ".join(str(j) for j in range(1, num_digits + 1))
    print(spaces + numbers)
