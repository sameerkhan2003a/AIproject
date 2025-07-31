# Original (stored) login credentials
original_username = "ramya"
original_password = "123"

# Ask user for input
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == original_username and password == original_password:
    print("Login successful!")
else:
    print("Login failed.Incorrect username or password.")