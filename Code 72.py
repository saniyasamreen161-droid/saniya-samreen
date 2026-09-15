n = int(input("Enter binary number: "))

decimal = 0
power = 0

while n > 0:
    digit = n % 10
    decimal = decimal + digit * (2 ** power)
    power = power + 1
    n = n // 10

print("Decimal =", decimal)
