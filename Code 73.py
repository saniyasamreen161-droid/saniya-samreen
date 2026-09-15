sum = 0
count = 0

while True:
    n = int(input("Enter number: "))

    if n == -1:
        break

    sum = sum + n
    count = count + 1

print("Count =", count)

if count > 0:
    print("Average =", sum / count)
