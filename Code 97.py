n = 4
for i in range(1, n + 1):
    row = [str((j - 1) % 2) for j in range(1, i + 1)]
    print(" ".join(row))
