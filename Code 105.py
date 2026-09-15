n = 4
for i in range(1, n + 1):
    spaces = " " * (2 * (n - i))
    nums = [str(j) for j in range(1, i + 1)] + [str(j) for j in range(i - 1, 0, -1)]
    print(spaces + " ".join(nums))
for i in range(n - 1, 0, -1):
    spaces = " " * (2 * (n - i))
    nums = [str(j) for j in range(1, i + 1)] + [str(j) for j in range(i - 1, 0, -1)]
    print(spaces + " ".join(nums))
