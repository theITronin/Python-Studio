# --- Creation and Basic Access ---
numbers = [10, 5, 7, 2, 1]  # List creation
print(numbers[0])  # Output: 10 (first element)
print(numbers[4])  # Output: 1 (last element)

# --- Direct Assignment Modification ---
numbers[0] = 111
print(numbers)  # Output: [111, 5, 7, 2, 1]

# --- Copying between Elements ---
numbers[1] = numbers[4]
print(numbers)  # Output: [111, 1, 7, 2, 1]

# --- Deleting with 'del' ---
del numbers[1]
print(numbers)  # Output: [111, 7, 2, 1]

# --- Functions vs Methods ---
print(len(numbers))  # Output: 4 (current length using function)

numbers.append(4)
print(numbers)  # Output: [111, 7, 2, 1, 4] (.append method)

numbers.insert(0, 222)
print(numbers)  # Output: [222, 111, 7, 2, 1, 4] (.insert method)

# --- Negative Indices ---
print(numbers[-1])  # Output: 4 (last element)
print(numbers[-2])  # Output: 1 (second to last element)

# --- Dynamic List Building ---
# Using .append() -> Adds to the end
my_list = []
for i in range(5):
    my_list.append(i + 1)
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Using .insert() -> Inserts at the beginning
my_list = []
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)  # Output: [5, 4, 3, 2, 1]

# --- Iteration over Lists ---
# Method 1: Using Indices
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)  # Output: 15 (sum of elements)

# Method 2: Direct Iteration (Pythonic way)
total = 0
for num in my_list:
    total += num
print(total)  # Output: 15

# --- Advanced Operations ---
# Traditional variable swap
a, b = 1, 2
a, b = b, a  # Now a=2, b=1

# List elements swap
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
print(my_list)  # Output: [5, 1, 8, 3, 10]

# Reversing a list manually
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# Cumulative Sum Algorithm
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)  # Output: [1, 3, 6, 10, 15]