# 1. Tuples: Immutable Sequences

# Key Characteristics:
# - Syntax: Defined using parentheses or simply by separating values with commas
tuple_1 = (1, 2, 3)  # Traditional form
tuple_2 = 1, 2, 3     # Simplified form

# - Immutability: Elements cannot be altered after the tuple has been instantiated
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Would cause a type error: TypeError

# - Special initialization cases:
empty_tuple = ()          # Creating an empty tuple
single_element = (1,)     # Tuple with a single element (the comma is mandatory!)

# Common Operations with Tuples:
my_tuple = (1, 10, 100)

# Indexing and slicing
print(my_tuple[0])    # Output: 1
print(my_tuple[-1])   # Output: 100
print(my_tuple[1:])   # Output: (10, 100)

# Concatenation and repetition
new_tuple = my_tuple + (1000, 10000)
repeat_tuple = my_tuple * 3

# Useful functions and membership operators
print(len(my_tuple))          # Output: 3
print(10 in my_tuple)         # Output: True
print(5 not in my_tuple)      # Output: True


# 2. Dictionaries and Combined Structures
# Practical Case Study: Managing School Grades
school_class = {}

# Mock structure to simulate continuous user inputs
input_data = [("Ana", 9), ("Luis", 8), ("Ana", 10)]

for name, score in input_data:
    if name in school_class:
        school_class[name] += (score,)  # Appends the grade by concatenating tuples
    else:
        school_class[name] = (score,)   # Initializes the key with a single-element tuple

# Processing and calculating academic results
for name in sorted(school_class.keys()):
    total = sum(school_class[name])
    count = len(school_class[name])
    print(f"{name}: {total/count:.2f}")

# Advantages of this Combined Design:
# 1. Dictionary: Provides instant access to grades indexed by student name.
# 2. Tuples: Safely store collections of immutable data efficiently.
# 3. Sorting: Cleanly displays results alphabetically using sorted().


# 5. Best Practices
# - Tuples: Use them when you need to ensure data does not change; they consume less memory.
# - Dictionaries: Use meaningful, readable keys; employ .get() to prevent KeyError exceptions:
#   value = dictionary.get("key", default_value)