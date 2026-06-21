# 1. Basic try-except Structure
# Exceptions are runtime anomalies. Code that might fail goes inside 'try'.
# If an error occurs, execution jumps to the 'except' block to handle it.
try:
    value = int(input("Enter an integer: "))
    print(100 / value)
except:
    print("An error occurred during execution.")


# 2. Multiple Specific Except Blocks
# You can handle different exceptions by specifying their names.
# Only the first matching except block will execute.
try:
    lst = [1, 2, 3]
    print(lst[5])  # Throws IndexError
except ValueError:
    print("Handling an invalid value conversion.")
except IndexError:
    print("Handling an out-of-bounds list access.")


# 3. The Default/Anonymous Except Block
# An anonymous/unnamed except block catches any exception not caught before.
# It MUST always be placed at the very end of all specific except blocks.
try:
    num = int("not a number")
except IndexError:
    print("This won't catch it.")
except:
    print("This anonymous block catches everything else.")


# 4. Exception Hierarchy & Ordering
# Built-in exceptions form a hierarchy tree. More specific exceptions must 
# always be placed BEFORE general exceptions (e.g., IndexError before LookupError).

# Correct Ordering:
try:
    lst = [10]
    print(lst[9])
except IndexError:
    print("Specific list error handled first.")
except LookupError:
    print("General lookup error handled second.")

# Incorrect Ordering (Inaccessible Code):
try:
    lst = [10]
    print(lst[9])
except LookupError:
    print("This runs because LookupError is the parent of IndexError.")
except IndexError:
    pass  # Critical: This line is unreachable code and will never run!


# 5. Raising Exceptions (raise)
# The 'raise' keyword triggers an exception manually on demand.
# 'raise' without a name can only be used inside 'except' to re-raise the current error.
try:
    raise ValueError("Manual Error")
except ValueError:
    print("Caught manual error.")
    # raise  # Re-raises the ValueError to the outside scope if uncommented


# 6. Assertions (assert)
# 'assert expression' evaluates a condition. If it is falsy (0, "", None, False), 
# it immediately raises an AssertionError exception. Used to secure critical data.
def calculate_age(year):
    assert year > 0, "Year must be greater than zero!"
    return 2026 - year


# 7. Built-in Exceptions Reference 
# Abstract / General Exceptions (used as parent classes):
# - BaseException (The absolute top root of all exceptions)
# - ArithmeticError (Base class for math errors)
# - LookupError (Base class for search/indexing errors)

# Concrete Exceptions (specific errors raised at runtime):
# - AssertionError (Raised when an assert statement fails)
# - ImportError (Raised when an import statement fails to load a module)
# - IndexError (Raised when a sequence subscript is out of range)
# - KeyboardInterrupt (Raised when the user hits interrupt keys like Ctrl+C)
# - KeyError (Raised when a dictionary key is not found)
# - MemoryError (Raised when an operation runs out of memory)
# - OverflowError (Raised when a math result is too large to be represented)