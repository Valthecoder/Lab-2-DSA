def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

base = int(input("Enter a number you want to multiply by itself(base): "))
exponent = int(input("Enter the number of times you want the base to be multiplied(exponent): "))
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
    