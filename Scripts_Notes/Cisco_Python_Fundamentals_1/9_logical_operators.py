# --- AND Operator truth table ---
print(False and False)  # Output: False
print(False and True)   # Output: False
print(True and False)   # Output: False
print(True and True)    # Output: True

# --- OR Operator truth table ---
print(False or False)  # Output: False
print(False or True)   # Output: True
print(True or False)   # Output: True
print(True or True)    # Output: True

# --- NOT Operator truth table ---
print(not False)  # Output: True
print(not True)   # Output: False

# --- Comparison with NOT ---
var = 1
print(var > 0)         # Output: True
print(not (var <= 0))  # Output: True (logical equivalent)

# --- Alternative Comparison ---
var = 1
print(var != 0)        # Output: True
print(not (var == 0))  # Output: True (logical equivalent)

# --- Bitwise Operators ---
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print(a & b)  # Output: 1 (0001) -> Bitwise AND
print(a | b)  # Output: 7 (0111) -> Bitwise OR
print(a ^ b)  # Output: 6 (0110) -> Bitwise XOR
print(~a)     # Output: -6 (two's complement) -> Bitwise NOT

# --- Advanced Application: Bit Flags Manipulation ---
flag_register = 0b00000000  # Initial register (8 bits)
the_mask = 0b00001000       # Mask for bit 3 (starting from 0)

# 1. Verify bit state
if flag_register & the_mask:
    print("Bit 3 is 1")
else:
    print("Bit 3 is 0")

# 2. Reset bit to 0
flag_register &= ~the_mask

# 3. Set bit to 1
flag_register |= the_mask

# 4. Toggle bit
flag_register ^= the_mask

# --- Interactive Example: Logical vs Numeric Values ---
a = 5  # True (non-zero)
b = 0  # False (zero)

# Logical operations return the last evaluated value
print(a or b)  # Output: 5 (equivalent to True)
print(b or a)  # Output: 5
print(not a)   # Output: False
print(not b)   # Output: True