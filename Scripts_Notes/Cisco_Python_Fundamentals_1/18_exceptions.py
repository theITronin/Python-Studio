
# 1. Fundamental Concepts of Exceptions
# Exceptions represent anomalous events that interrupt the normal execution flow.
# Error Distinction:
# 1. Syntax Errors: Structural errors detected at compile time (e.g., a missing ':').
# 2. Exceptions: Logical errors produced at runtime (e.g., division by zero).


# 2. Basic try-except Structure
try:
    # Instructions block prone to errors
    value = int(input('Enter a number: '))
    print(1 / value)
except:
    # Generic catch statement if any exception occurs
    print('An error occurred')


# 3. Handling and Catching Multiple Specific Exceptions
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1 / value)        
except ValueError:
    print('Not a valid number')    # Data conversion error
except ZeroDivisionError:
    print('Cannot divide by zero') # Arithmetic division error

# Ordering Rule: Always list exception blocks from most specific to most general.


# Using Optional Blocks: 'else' and 'finally'
try:
    print("Simulating resource allocation/opening...")
    # If a FileNotFoundError occurred, it would jump straight to the except block
except FileNotFoundError:
    print("File not found")
else:
    print("Read successful")  # Executes ONLY if NO exception occurred
finally:
    print("Resource cleanup") # ALWAYS executes, regardless of exceptions


# Manually Raising Exceptions ('raise')
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")  # Intentionally triggers an exception
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(e)  # Prints the custom message provided inside the raise statement


# Debugging vs Exception Handling
# - Debugging: Fixing technical bugs in code during the development phase (e.g., using debuggers/prints).
# - Exception Handling: Safely handling anticipated runtime environment or user anomalies in production (try-except).


# Practical Structured Exercise
def calculate_average(numbers):
    try:
        if not numbers:
            raise ValueError("The list cannot be empty")
        return sum(numbers) / len(numbers)
    except TypeError:
        print("Error: You must provide a list of numbers")
    except ZeroDivisionError:
        print("Error: The list cannot be empty")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Validation cases for the exercise:
calculate_average([10, 20, 30])
calculate_average([])           # Throws a controlled exception