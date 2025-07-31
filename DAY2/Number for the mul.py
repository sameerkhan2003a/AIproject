# Ask user to enter a number for the multiplication table
number = int(input("Enter a number to print its multiplication table: "))

# Ask user how many multiples they want
limit = int(input("Enter the range (e.g., 10 for table up to 10): "))

print(f"\n📘 Multiplication Table of {number} up to {limit}:\n")

# Print the multiplication table
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")