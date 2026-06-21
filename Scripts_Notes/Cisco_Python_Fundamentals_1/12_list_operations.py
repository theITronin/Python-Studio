# --- 1. References vs List Copies ---
list_1 = [1]
list_2 = list_1  # This creates a reference, not a copy
list_1[0] = 2
print(list_2)  # Output: [2] (both variables point to the same list object)

# --- 2. Slicing for Independent Copies ---
list_1 = [1]
list_2 = list_1[:]  # This creates a completely independent copy
list_1[0] = 2
print(list_2)  # Output: [1] (the copy is not modified)

# --- 3. Practical Slicing Examples ---
my_list = [10, 8, 6, 4, 2]

# Partial copy
print(my_list[1:3])  # Output: [8, 6]

# Slicing with negative indices
print(my_list[1:-1])  # Output: [8, 6, 4]

# Omitting indices
print(my_list[:3])  # Output: [10, 8, 6]
print(my_list[3:])  # Output: [4, 2]

# --- 4. Deleting with 'del' and Slicing ---
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]  # Deletes elements at positions 1 and 2
print(my_list)  # Output: [10, 4, 2]

# --- Membership Operators (in and not in) ---
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)     # Output: False
print(5 not in my_list) # Output: True
print(12 in my_list)    # Output: True

# --- Common Algorithms with Lists ---
# 1. Finding the Maximum Value (Index Version)
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)  # Output: 17

# Finding Maximum (Pythonic direct iteration version)
largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num
print(largest)

# Finding Maximum (Slicing iteration version)
largest = my_list[0]
for num in my_list[1:]:
    if num > largest:
        largest = num
print(largest)

# 2. Searching for an Element in a List
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    if my_list[i] == to_find:
        found = True
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

# 3. List Intersection (Lottery Example)
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)  # Output: 4 (matched numbers)