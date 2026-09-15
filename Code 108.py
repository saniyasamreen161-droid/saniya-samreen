n = 5

for i in range(n):
    for j in range(n):
        # Print top half (upper line to middle tip)
        if i <= n // 2:
            if j == n - 1 or j == n - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        # Print bottom half (middle tip down to lower line)
        else:
            if j == n - 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
    print()
