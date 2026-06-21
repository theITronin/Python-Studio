# --- 1. return without expression (Early Termination) ---
def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return  # Immediately exits the function (returns None)
    print("Happy New Year!")

happy_new_year(False)

# --- 2. return with expression ---
def boring_function():
    return 123

x = boring_function()
print(x)  # Output: 123

# --- Practical Use Cases ---
# Calculation and Return of Results
def calculate_rectangle_area(base, height):
    return base * height

area = calculate_rectangle_area(5, 10)
print(area)  # Output: 50

# Validation with Early Return
def is_positive(num):
    if num <= 0:
        return False
    return True  # Only executes if num > 0

# --- Functions processing Lists ---
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

print(list_sum([5, 4, 3]))  # Output: 12

# Error Handling in Functions
def safe_list_sum(lst):
    if not isinstance(lst, list):
        return "Error: A list was expected"
    return sum(lst)

print(safe_list_sum(5))  # Output: Error: A list was expected

# List Generation Functions
def generate_list(n):
    return [i for i in range(n, -1, -1)]

print(generate_list(4))  # Output: [4, 3, 2, 1, 0]

# --- Advanced Example: Multiple Return Values (Tuples) ---
def calculate_operations(a, b):
    total_sum = a + b
    difference = a - b
    return total_sum, difference  # Returns a tuple implicitly

results = calculate_operations(10, 5)
print(results)  # Output: (15, 5)