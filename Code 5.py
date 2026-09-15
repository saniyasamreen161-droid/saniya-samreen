n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0:
    print("Disivible by 3")
elif n % 5 == 0:
    print("Disivible by 5")

else:
    print("Not divisible by both 3 and 5")
