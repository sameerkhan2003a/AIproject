# Input from user
number = int(input("Enter a number: "))

# Initialize reversed number
reversed_number = 0

# Store original number for display if needed
original_number = number

# Reverse the number using while loop
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

# Output the result
print("Reversed number is:", reversed_number)