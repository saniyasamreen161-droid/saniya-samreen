c = float(input("Enter temperature in Celsius: "))
f = float(input("Enter temperature in Fahrenheit: "))

f = (c * 9 / 5) + 32
c = (f - 32) * 5 / 9

print("Fahrenheit =", f)
print("Celsius =", c)
