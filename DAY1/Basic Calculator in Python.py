# Basic Calculator in Python

# Get inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get the operation
print("Choose operation: +  -  *  /")
operation = input("Enter operation: ")

# Perform the calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

# Show result
print("Result:", result)