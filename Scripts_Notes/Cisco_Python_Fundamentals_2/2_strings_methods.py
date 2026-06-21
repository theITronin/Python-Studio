# 1. String Fundamentals & Multi-line Strings 
# Strings are immutable sequences. They can be indexed, sliced, iterated, 
# and support membership operators ('in' and 'not in').
single_line_1 = 'Single line string'
single_line_2 = "Another single line string"

multi_line_1 = '''This is a multi-line string.
It can cross line boundaries in the source code.'''

multi_line_2 = """Another multi-line string
using triple double-quotes."""


# 2. String Length & Escape Characters
# The len() function returns the number of characters. 
# Escape characters (like '\n') count as a single character.
print(len("\n\n"))  # Output: 2 (each '\n' is one character)


# 3. Concatenation and Replication
# Strings can be merged with '+' and duplicated with '*'.
asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)  # Output: *+*+*+*+*


# 4. Code Points: chr() and ord()
# ord() returns the ASCII/Unicode code point of a character.
# chr() returns the character corresponding to a code point.
print(ord('A'))      # Output: 65
print(chr(65))      # Output: 'A'
# Always true: chr(ord(ch)) == ch AND ord(chr(cp)) == cp


# 5. Built-in Functions applied to Strings
word = "Python"
print(list(word))  # Output: ['P', 'y', 't', 'h', 'o', 'n']
print(max(word))   # Output: 'y' (highest Unicode code point)
print(min(word))   # Output: 'P' (lowest Unicode code point)


# 6. String Search & Modification Methods
text = "hello World"

print(text.index("lo"))     # Output: 3 (returns first index found or ValueError)
print(text.capitalize())    # Output: 'Hello world' (only first character to upper)
print(text.center(20, "-")) # Output: '----hello World-----' (centers string)
print(text.count("l"))      # Output: 3 (counts occurrences)
print("-".join(["a", "b"])) # Output: 'a-b' (joins sequence items into a string)
print(text.lower())         # Output: 'hello world' (all to lowercase)
print("  abc  ".lstrip())   # Output: 'abc  ' (removes leading whitespaces)
print(text.replace("o", "X")) # Output: 'hellX WXrld' (replaces substring)
print("hello".rfind("l"))   # Output: 3 (finds substring starting from the end)
print("  abc  ".rstrip())   # Output: '  abc' (removes trailing whitespaces)
print("a,b,c".split(","))   # Output: ['a', 'b', 'c'] (splits string into a list)
print("  abc  ".strip())    # Output: 'abc' (removes leading and trailing spaces)
print(text.swapcase())      # Output: 'HELLO wORLD' (swaps case of all letters)
print(text.title())         # Output: 'Hello World' (capitalizes first letter of each word)
print(text.upper())         # Output: 'HELLO WORLD' (all to uppercase)


# 7. String Content Validation (Boolean Methods)
print("python".endswith("on"))   # Output: True
print("abc123".isalnum())        # Output: True (only letters and digits)
print("abc".isalpha())           # Output: True (only letters)
print("abc".islower())           # Output: True (only lowercase letters)
print("   ".isspace())           # Output: True (only whitespaces)
print("ABC".isupper())           # Output: True (only uppercase letters)
print("python".startswith("py")) # Output: True


# 8. String Comparisons
# Strings can be compared with each other. Comparing them with numbers 
# does not throw errors for equality but will not yield reasonable results.
print("abc" == 123)  # Output: False (string == number is always False)
print("abc" != 123)  # Output: True  (string != number is always True)
# print("abc" >= 123) # Critical: Throws a TypeError exception!


# 9. Sorting Strings
names = ["Charlie", "Alpha", "Beta"]

# sorted() returns a new sorted list
sorted_names = sorted(names) 
print(sorted_names)  # Output: ['Alpha', 'Beta', 'Charlie']

# .sort() modifies the list in place
names.sort()
print(names)         # Output: ['Alpha', 'Beta', 'Charlie']


# 10. String Type Conversions
print(str(100))      # Output: '100' (number to string)
print(int("123"))    # Output: 123 (string to integer)
print(float("12.3")) # Output: 12.3 (string to float)
# Note: Type conversion fails and throws an exception if string is invalid (e.g., int("abc"))