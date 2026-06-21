# --- Exponentiation Operator (**) ---
print(2 ** 3)        # 8 (integer)
print(2 ** 3.)       # 8.0 (float because one operand is a float)
print(2. ** 3)       # 8.0 (float because one operand is a float)
print(2. ** 3.)      # 8.0 (both are floats)

# --- Multiplication Operator (*) ---
print(2 * 3)         # 6 (integer)
print(2 * 3.)        # 6.0 (float because one operand is a float)
print(2. * 3)        # 6.0 (float because one operand is a float)
print(2. * 3.)       # 6.0 (both are floats)

# --- Division Operator (/) ---
print(6 / 3)         # 2.0 (standard division always returns a float)
print(6 / 3.)        # 2.0
print(6. / 3)        # 2.0
print(6. / 3.)       # 2.0

# --- Integer Division (//) ---
print(6 // 3)        # 2 (integer)
print(6 // 3.)       # 2.0 (returns float if any operand is a float)
print(6. // 3)       # 2.0
print(6. // 3.)      # 2.0
print(6 // 4)        # 1 (rounds down to the nearest whole integer)
print(6. // 4)       # 1.0
print(-6 // 4)       # -2 (rounds down towards negative infinity for negative numbers)
print(6. // -4)      # -2.0

# --- Modulo Operator (%) ---
print(14 % 4)        # 2 (returns the remainder: 14 - (3*4) = 2)
print(12 % 4.5)      # 3.0 (returns a float if any operand is a float)

# --- Addition and Subtraction Operators ---
print(-4 + 4)        # 0 (integer)
print(-4. + 8)       # 4.0 (float because one operand is a float)
print(-4 - 4)        # -8 (integer)
print(4. - 8)        # -4.0 (float because one operand is a float)
print(-1.1)          # -1.1 (unary minus creating a negative float literal)

# --- Operator Precedence ---
print(2 + 3 * 5)     # 17 (multiplication has higher precedence than addition)
print(9 % 6 % 2)     # 1 (left-sided associativity: (9 % 6) % 2)
print(2 ** 2 ** 3)   # 256 (right-sided associativity: 2 ** (2 ** 3))
print(-3 ** 2)       # -9 (exponentiation has higher precedence than the unary minus sign)
print(-2 ** 3)       # -8
print(-(3 ** 2))     # -9 (explicit grouping equivalent to the above expression)

# --- Complex Expression ---
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)  # Evaluates step-by-step to 10.0
# Steps: 1. 25%13=12 -> 2. 12+100=112 -> 3. 5*112=560 -> 4. 2*13=26 -> 5. 560/26≈21.53 -> 6. 21.53//2=10.0