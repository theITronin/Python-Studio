# --- Naming Rules for Variables ---
# - Can contain UPPERCASE, lowercase, digits, and underscores (_)
# - Must begin with a letter or an underscore (_)
# - Case-sensitive (var and Var are different variables)
# - Cannot be a Python reserved word / keyword

# --- Variable Declaration and Basic Usage ---
var = 1
print(var)  # Output: 1

account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)  # Output: 1 1000.0 John Doe
print(var)  # Output: 1

var = "3.8.5"
print("Python version: " + var)  # Output: Python version: 3.8.5

# --- Variable Reassignment ---
var = 1
print(var)  # Output: 1
var = var + 1
print(var)  # Output: 2

# --- Mathematical Application (Pythagorean Theorem) ---
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)  # Output: c = 5.0

# --- Shorthand Assignment Operators ---
x = 1
x = x * 2  # Standard math update: x = 2
x *= 2     # Shorthand operator: x = 4

sheep = 1
sheep = sheep + 1  # Standard math update: sheep = 2
sheep += 1         # Shorthand operator: sheep = 3

# --- Example 1: Miles to Kilometers Conversion ---
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles are", round(miles_to_kilometers, 2), "kilometers")  
print(kilometers, "kilometers are", round(kilometers_to_miles, 2), "miles")  

# --- Example 2: Polynomial Expression Evaluation ---
x = 1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)  # Output: y = 3.0