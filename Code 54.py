n = int(input("Enter number: "))

div = 1

while n // div >= 10:
    div = div * 10

while div > 0:
    print(n // div)
    n = n % div
    div = div // 10
