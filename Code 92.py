n = 4
for i in range(n):
    print(" " * (n - i - 1), end="")
    val = 1
    row = []
    for k in range(i + 1):
        row.append(str(val))
        val = val * (i - k) // (k + 1)
    print(" ".join(row))
