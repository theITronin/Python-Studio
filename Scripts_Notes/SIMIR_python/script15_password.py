# variable declaration
password = str(input("Enter your password (8 characters minimum): "))

# Condiciones
if len(password) < 8:
    print("The password must be at least 8 characters long.")
else:
    print(f"Password: {password} saved")