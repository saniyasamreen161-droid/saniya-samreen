n = 4
for i in range(1, n + 1):
    spaces = " " * (2 * (n - i))
    row = " ".join(chr(65 + j) for j in range(i))
    print(spaces + row)
