# --- Comparing Two Numbers ---
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
print("The larger number is:", larger_number)

# --- Comparing Three Numbers (Method 1: Conditional Checks) ---
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = number1  # Baseline setting
if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
print("The largest number is:", largest_number)

# --- Comparing Three Numbers (Method 2: max() function) ---
largest_number = max(number1, number2, number3)  # Optimized native max approach.
print("The largest number is:", largest_number)

# --- Finding the Smallest Number ---
smallest_number = min(number1, number2, number3)  # Uses min() function to find the minimum.
print("The smallest number is:", smallest_number)

# --- Case-Sensitive String Conditionals ---
name = input("Enter the name of the flower: ")

if name == "SPATHIPHYLLUM":
    print("Yes, SPATHIPHYLLUM is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big SPATHIPHYLLUM!")
else:
    print("SPATHIPHYLLUM!, Not", name + "!")