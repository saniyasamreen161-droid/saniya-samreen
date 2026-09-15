# Upper half of the heart
for i in range(1, 3):
    print(" " * (2 - i) + "*" * (2 * i + 1) + " " * (5 - 2 * i) + "*" * (2 * i + 1))

# Lower half of the heart
for i in range(7, 0, -2):
    print(" " * ((9 - i) // 2) + "*" * i)
