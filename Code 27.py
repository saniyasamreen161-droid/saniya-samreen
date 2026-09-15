units = int(input("Enter units: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100 + (units - 100) * 2
else:
    bill = 300 + (units - 200) * 3

print("Electricity bill =", bill)
