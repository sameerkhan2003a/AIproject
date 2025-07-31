from datetime import date

# Get the current year
current_year = date.today().year

# Ask the user to enter their birth year
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = current_year - birth_year

# Display result
print(f"You are {age} years old.")