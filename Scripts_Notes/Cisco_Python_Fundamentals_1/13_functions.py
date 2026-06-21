# --- 1. Basic Function Definition ---
def message():
    print("Enter value: ")

message()  # Calls the function

# --- 2. Parameters and Arguments ---
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Carlos")  # 'Carlos' is an argument

# --- 3. Multiple Parameters ---
def message(what, number):
    print("Enter", what, "number", number)

message("phone", 11)

# --- Argument Passing Types ---
# Method 1: Positional Arguments (by order)
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")

# Method 2: Keyword Arguments
introduction(last_name="Skywalker", first_name="Luke")  # Order doesn't matter

# Method 3: Mixed Arguments (positional + keywords)
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, c=1, b=2)  # 3 is positional, b and c are keywords. Rule: positionals first!

# --- Default Parameters ---
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction("Enrique")  # Uses default "Smith" for last_name

# --- Advanced Concepts: Shadowing ---
number = 1234
def message(number):
    print("Enter a number:", number)

message(1)     # Prints internal parameter value: 1
print(number)  # Prints global variable value: 1234

# --- Practical Examples ---
# Centralized Reusable Function
def input_message():
    print("Please enter a value:")

input_message()
a = int(input())
input_message()
b = int(input())

# Function with Calculation Logic
def calculate_sum(a, b, c):
    return a + b + c

result = calculate_sum(3, 5, 2)
print(result)  # Output: 10

# --- Common Errors ---
# Error 1: Calling a function before defining it
# greet_error()  # Causes Error!
# def greet_error():
#     print("Hello")

# Error 2: Duplicate names overwriting functions
def duplicate_message():
    print("Hello")

duplicate_message = 123  # This overwrites the function with an integer!