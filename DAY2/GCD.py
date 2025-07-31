# Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Make sure a and b are positive
a = abs(a)
b = abs(b)

# Use while loop to find GCD
while b != 0:
    temp = b
    b = a % b
    a = temp

# Output the result
print("GCD is:", a)