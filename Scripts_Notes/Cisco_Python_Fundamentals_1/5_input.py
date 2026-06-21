# --- Basic Input Function ---
print("Tell me anything...")
anything = input()  # Pauses code execution and waits for user text entry.
print("Hmm...", anything, "... really?")

# --- Input with Integrated Prompt Message ---
anything = input("Tell me anything...")  # Direct message shortens code.
print("Hmm...", anything, "...really?")

# --- Conversion to Float ---
anything = float(input("Enter a number: "))  # Converts text input to a float decimal.
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# --- Conversion to Integer ---
anything = int(input("Enter a number: "))  # Converts to integer; crashes if decimal is typed.
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# --- Interactive Pythagorean Theorem ---
leg_a = float(input("Enter the first leg length: "))
leg_b = float(input("Enter the second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("The length of the hypotenuse is:", hypo)

# --- Capturing Strings and Concatenating ---
fnam = input("Can you give me your first name please? ")
lnam = input("Can you give me your last name please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")  # Combines strings using '+'

# --- ASCII Art with String Replication ---
print("+" + 10 * "-" + "+")  # Generates 10 dashes dynamically.
print(("|" + " " * 10 + "|\n") * 5, end="")  # Replicates rows to build the side walls.
print("+" + 10 * "-" + "+")

# --- Alternative Interactive Pythagorean Theorem ---
leg_a = float(input("Enter the first leg length: "))
leg_b = float(input("Enter the second leg length: "))
print("The length of the hypotenuse is " + str((leg_a**2 + leg_b**2) ** .5))  # Casts result to string.