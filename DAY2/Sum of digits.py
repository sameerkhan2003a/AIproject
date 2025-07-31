# Input from user
number = int(input("Enter a number: "))

# Initialize sum variable
sum_of_digits = 0

# Use while loop to extract digits and sum them
while number > 0:
    digit = number % 10        
    sum_of_digits += digit      
    number = number // 10      

# Output the result
print("Sum of digits is:", sum_of_digits)