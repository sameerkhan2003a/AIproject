# Input from user
number = int(input("Enter a number: "))

# Initialize factorial value
factorial = 1

# Calculate factorial using for loop
for i in range(1, number + 1):
    factorial *= i

# Output the result
print("Factorial of", number, "is:", factorial)