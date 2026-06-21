# --- Difference between string and integer ---
print("2")  # This is a string argument.
print(2)    # This is a literal integer number.

# --- Advanced numeric formats ---
print(1_000_000)   # Large numbers with underscores for readability.
print(+1_000_000)  # The plus sign indicates it is positive (redundant).
print(-1_000_000)  # The minus sign indicates a negative number.

# --- Alternative number systems ---
print(0o123)  # '0o' prefix for octal numbers (base 8). 0o123 octal = 83 decimal.
print(0x123)  # '0x' prefix for hexadecimal numbers (base 16). 0x123 hex = 291 decimal.

# --- Floating-point numbers ---
print(0.5)  # Standard float literal.
print(.5)   # The leading zero can be omitted.
print(8.0)  # Float with a zero decimal.
print(8.)   # Shortened form of a float.

# --- Scientific notation ---
print(300000000) 
print(3e8)  # 'e' indicates exponent (3 × 10^8).
print(0.0000000000000000000001)
print(1e-22)  # Negative scientific notation (1 × 10^-22).
print(6.62607e-34)  # Physical constant (Planck's constant).

# --- Strings and special characters ---
print("I like \"Monty Python\"")  # Escape quotes inside a string using \
print("\"I am\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")  # \n creates line breaks.

# --- Boolean values ---
print(True > False)  # True counts as 1, False counts as 0 (1 > 0 → True).
print(True < False)  # 1 < 0 → False.

# --- Combining alternate bases ---
print(0o123 + 0x123)  # Adding octal and hexadecimal numbers directly: 83 + 291 = 374.