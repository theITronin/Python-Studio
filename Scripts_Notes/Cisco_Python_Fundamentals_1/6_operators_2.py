# --- Equality Operator (==) ---
var = 0
print(var == 0)  # Output: True (compares if two values are equal)

var = 1
print(var == 0)  # Output: False

# --- Inequality Operator (!=) ---
var = 0
print(var != 0)  # Output: False (checks if two values are different)

var = 1
print(var != 0)  # Output: True

# --- Greater Than (>) and Greater Than or Equal To (>=) ---
black_sheep = 5
white_sheep = 2
print(black_sheep > white_sheep)  # Output: True

centigrade_outside = 42
print(centigrade_outside >= 0.0)  # Output: True

# --- Less Than (<) and Less Than or Equal To (<=) ---
current_velocity_mph = 85
print(current_velocity_mph < 85)  # Output: False
print(current_velocity_mph <= 85)  # Output: True

# --- Storing Comparison Results ---
number_of_lions = 10
number_of_lionesses = 7
answer = number_of_lions >= number_of_lionesses  # Assigns boolean directly (True)

# --- Operator Priority Table Summary (Highest to Lowest) ---
# 1. Unary signs (+x, -x)
# 2. Exponentiation (**)
# 3. Multiplicative operations (*, /, //, %)
# 4. Additive operations (+, -)
# 5. Logical comparisons (<, <=, >, >=)
# 6. Equality validations (==, !=)