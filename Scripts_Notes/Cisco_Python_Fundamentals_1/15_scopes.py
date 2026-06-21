# Fundamental Concepts of Scope in Python

# 1. Variable Scope

# Local Variable (defined inside a function):
def scope_test():
    x = 123  # Local variable

scope_test()
# print(x)  # Would cause an Error: x is not defined outside the function

# Global Variable (accessible from anywhere, including inside functions):
var = 1  # Global variable

def my_function():
    print("Do I know the variable?", var)  # Accesses the global variable

my_function()  # Output: Do I know the variable? 1
print(var)     # Output: 1


# 2. Shadowing (Hiding Variables)
var = 1  # Global

def my_function_shadow():
    var = 2  # Local (temporarily hides the global variable)
    print("Inside:", var)

my_function_shadow()  # Output: Inside: 2
print("Outside:", var)  # Output: Outside: 1

# Behavior: The local variable 'var' hides the global one within the function's scope.


# Using the 'global' Keyword
# Explicitly Modifying Global Variables:
var = 1

def my_function_global():
    global var  # Tells Python we will use and modify the global variable
    var = 2     # Directly changes the global variable
    print("Inside:", var)

my_function_global()  # Output: Inside: 2
print("Outside:", var)  # Output: Outside: 2 (The global variable has changed!)

# Caution: Overusing 'global' can make the code difficult to maintain.


# Argument Passing
# With Scalar Values (Immutable types like integers or floats):
def my_function_scalar(n):
    n += 1  # Modifies only a local copy (creates a new local variable)
    print("Inside:", n)

var = 1
my_function_scalar(var)  # Output: Inside: 2
print("Outside:", var)     # Output: Outside: 1 (the original external variable remains unchanged)