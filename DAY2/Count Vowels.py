# Input from user
text = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize count
vowel_count = 0

# Loop through each character in the string
for char in text:
    if char in vowels:
        vowel_count += 1

# Output the result
print("Number of vowels in the string:", vowel_count)